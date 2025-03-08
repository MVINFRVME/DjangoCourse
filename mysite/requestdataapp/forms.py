from django import forms
from django.forms import Textarea


class UserBioForms(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(label='Your age')
    bio = forms.CharField(label='Biography', widget=Textarea)

