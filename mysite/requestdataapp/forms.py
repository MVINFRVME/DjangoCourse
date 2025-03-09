from django import forms
from django.forms import Textarea


class UserBioForms(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Your age', min_value=1, max_value=120)
    bio = forms.CharField(label='Biography', widget=Textarea)

