from .models import User, ProjectImage
from django.contrib.auth.forms import forms
from django.contrib.auth.hashers import make_password #For user creation


"""
===========
IMAGE FORM
===========
- project (fk)
- image (select multiple files)

"""
class ProjectImageForm(forms.ModelForm):
    class Meta:
        model= ProjectImage
        fields = [
            "project",
            "image",
        ]
        widgets = {
            "image": forms.ClearableFileInput()
        }
        labels = {
            "image":"Images"
        }