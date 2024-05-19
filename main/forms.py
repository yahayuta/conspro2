from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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

RentalOrderRowFormset = forms.inlineformset_factory(
    RentalOrder, RentalOrderRow, fields='__all__',
    extra=17, max_num=17
)
