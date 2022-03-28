from django import forms
from AppTwo import models

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'