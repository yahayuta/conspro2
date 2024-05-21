from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Inventory
from .models import Work, WorkRow
from .models import RentalOrder, RentalOrderRow

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class InventoryEditForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'sell_month': forms.NumberInput(attrs={"type":"date"}),
            'order_date': forms.NumberInput(attrs={"type":"date"}),
            'order_pay_date': forms.NumberInput(attrs={"type":"date"}),
            'sell_pay_date': forms.NumberInput(attrs={"type":"date"}),
        }

class WorkCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Work
        fields = '__all__'

WorkRowFormset = forms.inlineformset_factory(
    Work, WorkRow, fields='__all__',
    extra=17, max_num=17
)

class RentalOrderCreateForm(forms.ModelForm):

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

        # 新規登録の場合は在庫をレンタル出庫中に更新する
        if is_new_instance and rental_order.rental_inventory and rental_order.rental_inventory.status == '2':
            rental_order.rental_inventory.status = '3'
            rental_order.rental_inventory.save()

        # 返却日が設定されている場合空車にする
        if rental_order.in_date:
            rental_order.rental_inventory.status = '2'
            rental_order.rental_inventory.save()

        if commit:
            rental_order.save()
        return rental_order
    
RentalOrderRowFormset = forms.inlineformset_factory(
    RentalOrder, RentalOrderRow, fields='__all__',
    extra=17, max_num=17
)
