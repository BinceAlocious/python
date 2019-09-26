from django import forms

class FormName(forms.Form):
    name=forms.CharField(label="Name:")
    email=forms.EmailField(label="Email:")
    verify_email=forms.EmailField(label="Enter yor Email again:")
    text=forms.CharField(label="Enter Text:",widget=forms.Textarea)
