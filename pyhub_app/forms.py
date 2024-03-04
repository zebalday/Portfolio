from django.forms import ModelForm
from django import forms
from .models import GithubUser


class GithubUserForm(ModelForm):
    model = GithubUser
    fields = ['username']
    widgets = {
        'username': forms.TextInput(attrs={
            'class':'form-input',
            'placeholder':'Your github username',
            'maxlength':100,
            'pattern':'^[a-zA-Z0-9]{100}$'
        }),
    }
    labels = {
        'username':False
    }
    