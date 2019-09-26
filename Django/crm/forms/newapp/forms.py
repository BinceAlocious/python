from django import forms

class Employee(forms.Form):
    Empname=forms.CharField()
    desig=forms.CharField()
    sal=forms.IntegerField()


