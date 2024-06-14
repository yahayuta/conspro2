from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import Inventory, InventoryOrderRow
from .models import Work, WorkRow
from .models import RentalOrder, RentalOrderRow

# 年月用カスタムフィールド
class MonthYearField(forms.DateField):
    def to_python(self, value):
        if not value:
            return None
        try:
            return datetime.strptime(value, '%Y-%m').date()
        except ValueError:
            raise forms.ValidationError("日付を正しく入力してください。")

    def strptime(self, value, format):
        return datetime.strptime(value, format).date()

# 年月用カスタムWidget
class MonthYearWidget(forms.DateInput):
    input_type = 'month'

    def format_value(self, value):
        if value is None:
            return ''
        return value.strftime('%Y-%m')
    
# ログインフォーム
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# 在庫編集フォーム
class InventoryEditForm(forms.ModelForm):

    sell_month = MonthYearField(
        widget=MonthYearWidget(attrs={'type': 'month'}),
        label="売上月",
        required=False
    )
        
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'order_date': forms.NumberInput(attrs={"type":"date"}),
            'order_pay_date': forms.NumberInput(attrs={"type":"date"}),
            'sell_pay_date': forms.NumberInput(attrs={"type":"date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")

        # 現在のインスタンスのステータスをチェック
        if self.instance and self.instance.pk:
            current_status = Inventory.objects.get(pk=self.instance.pk).status
            if current_status == '3' and status != '3':
                raise forms.ValidationError("ステータスがレンタル出庫中の場合ステータスは変更できません")

        return cleaned_data
    
    def save(self, commit=True):
        inventory = super().save(commit=False)
        is_new_instance = self.instance.pk is None

        if commit:
            inventory.save()
        
        if is_new_instance:
            # Ensure Inventory is saved before creating InventoryOrderRow instances
            inventory.save()
            InventoryOrderRow.objects.create(inventory=inventory, name=f"{inventory.name}/{inventory.serial_no}", price=inventory.sell_price, total=inventory.sell_price)

        return inventory
    
# 在庫注文明細フォームセット
InventoryOrderRowFormset = forms.inlineformset_factory(
    Inventory, 
    InventoryOrderRow, 
    fields='__all__', 
    extra=17, 
    max_num=17
)

# 作業編集フォーム
class WorkEditForm(forms.ModelForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Work
        fields = '__all__'

# 作業明細編集フォーム
class WorkRowForm(forms.ModelForm):
    class Meta:
        model = WorkRow
        fields = '__all__'
        widgets = {
            'parts_delivery_date': forms.NumberInput(attrs={"type": "date"}),
        }

# 作業明細フォームセット
WorkRowFormset = forms.inlineformset_factory(
    Work, 
    WorkRow, 
    form=WorkRowForm,
    extra=17, 
    max_num=17
)

# レンタル注文編集フォーム
class RentalOrderEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RentalOrder
        fields = '__all__'
        widgets = {
            'out_date': forms.NumberInput(attrs={"type":"date"}),
            'in_date': forms.NumberInput(attrs={"type":"date"}),
            'start_date': forms.NumberInput(attrs={"type":"date"}),
            'end_date': forms.NumberInput(attrs={"type":"date"}),
            'request_date': forms.NumberInput(attrs={"type":"date"}),
        }

    def clean_rental_inventory(self):
        rental_inventory = self.cleaned_data.get('rental_inventory')
        is_new_instance = self.instance.pk is None
        if is_new_instance and rental_inventory and rental_inventory.status != '2':
            raise ValidationError('レンタル出庫不可能な在庫です')
        return rental_inventory
    
    def save(self, commit=True):
        rental_order = super().save(commit=False)

        is_new_instance = self.instance.pk is None

        # 返却日がもともと設定されていた場合かどうかの判定
        if not is_new_instance:
            existing_rental_order = RentalOrder.objects.get(pk=self.instance.pk)
            existing_in_date = existing_rental_order.in_date
        else:
            existing_in_date = None
            
        # 新規登録の場合は在庫をレンタル出庫中に更新する
        if is_new_instance and rental_order.rental_inventory and rental_order.rental_inventory.status == '2':
            rental_order.rental_inventory.status = '3'
            rental_order.rental_inventory.save()

            # 開始アワーをレンタル注文に設定しておく
            rental_order.hours_start = rental_order.rental_inventory.hours

        # 返却日が設定された場合空車にする
        if existing_in_date is None and rental_order.in_date and rental_order.rental_inventory.status == '3':
            rental_order.rental_inventory.status = '2'
            rental_order.rental_inventory.save()

        if commit:
            rental_order.save()
        
        if is_new_instance:
            if rental_order.order_type == '0':
                price = rental_order.rental_inventory.price_month
            elif rental_order.order_type == '1':
                price = rental_order.rental_inventory.price_day

            # Ensure RentalOrder is saved before creating RentalOrderRow instances
            rental_order.save()

            RentalOrderRow.objects.create(rental_order=rental_order, name="レンタル代", price=price)
            RentalOrderRow.objects.create(rental_order=rental_order, name="サポート料金", price=rental_order.rental_inventory.price_support)
            RentalOrderRow.objects.create(rental_order=rental_order, name="搬入運賃")
            RentalOrderRow.objects.create(rental_order=rental_order, name="返却運賃")

        return rental_order

# レンタル注文明細フォームセット
RentalOrderRowFormset = forms.inlineformset_factory(
    RentalOrder, 
    RentalOrderRow, 
    fields='__all__',
    extra=17, 
    max_num=17
)
