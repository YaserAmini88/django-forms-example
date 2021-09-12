from django import forms
from .models import formModel

class MyForm(forms.ModelForm):
    class Meta:
        model = formModel
        fields = ["email", "password",]
        labels = {'email': "Email Address", "password": "Password",}

