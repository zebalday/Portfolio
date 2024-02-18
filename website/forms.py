from .models import User
from django.contrib.auth.forms import forms
from django.contrib.auth.hashers import make_password #For user creation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        """ widgets = []
        labels = [] """