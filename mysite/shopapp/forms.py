from django import forms
from django.forms import Textarea


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(min_value=1, max_value=100_000)
    description = forms.CharField(label='Product description', widget=Textarea)

