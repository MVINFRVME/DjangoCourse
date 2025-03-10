from django import forms
from .models import Product


class ProductForm(forms.ModelForm): # ModelForm позволяет сгенерировать класс на основании существующей модели.
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount'
