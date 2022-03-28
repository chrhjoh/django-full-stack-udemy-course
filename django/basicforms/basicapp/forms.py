from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Your email Again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput, 
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("Emails does not match")