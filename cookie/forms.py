from django.db.models import fields
from .models import Cookie 
from django import forms

class CookieForm(forms.ModelForm):
    class Meta:
        model = Cookie
        fields = ['title', 'name', 'price', 'serial', 'body', 'image']


