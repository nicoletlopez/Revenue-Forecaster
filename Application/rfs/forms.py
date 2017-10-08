from django.contrib.auth.models import User
from django import forms
from .models import Project,File

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']

class FileForm(forms.ModelForm):

    class Meta:
        model=File
        fields=['excel_file']

class CreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['project_name'].widget.attrs = {'class': 'form-control'}
        self.fields['description'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model=Project
        fields=['project_name','description']


