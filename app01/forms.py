# -*- coding: utf-8 -*-
from django import forms 
from django.forms import fields
 
 
class UserForm(forms.Form):
    username = fields.CharField()
    email = fields.EmailField()

class SearchForm(forms.Form):
    query = forms.CharField(
    label='Enter a keyword to search for',
    widget=forms.TextInput(attrs={'size': 32})
    )