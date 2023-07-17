from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Inventory

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

