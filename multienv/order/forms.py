from django import forms

from models import Order

class OrderForm(forms.ModelForm):
    order_number = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input-medium', 'placeholder': 'Order Number'})
    )
    amount = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input-small', 'placeholder': 'Amount'})
    )
    class Meta:
        model = Order
    