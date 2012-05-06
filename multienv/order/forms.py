from django import forms

from core import utils
from order.models import Order

#===============================================================================
class OrderForm(forms.ModelForm):
    order_number = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input-medium', 'placeholder': 'Order Number'})
    )
    amount = forms.CharField(widget=forms.TextInput(
        attrs={'class':'input-small', 'placeholder': 'Amount'})
    )

    #===============================================================================
    class Meta:
        model = Order

    #---------------------------------------------------------------------------
    def save(self, request, *args, **kws):
        self.instance.ENV_DB = utils.get_environment(request)
        super(OrderForm, self).save(*args, **kws)

