from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm): # ModelForm позволяет сгенерировать класс на основании существующей модели.
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address', 'promocode', 'user', 'products'