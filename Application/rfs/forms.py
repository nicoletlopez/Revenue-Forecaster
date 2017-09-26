from django.contrib.auth.models import User
from django import forms
from .models import Project,File

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']

class FileForm(forms.ModelForm):

    class Meta:
        model=File
        fields=['excel_file']
