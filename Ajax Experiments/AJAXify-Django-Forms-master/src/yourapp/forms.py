# yourapp.forms.py
from django import forms

class JoinForm(forms.Form): # or forms.ModelForm
    email = forms.EmailField()
    name = forms.CharField(max_length=120)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == "abc@gmail.com":
            raise forms.ValidationError("This is not valid")
        return email