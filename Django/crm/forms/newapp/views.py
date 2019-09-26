from django.shortcuts import render
from django.contrib import messages
from newapp.models import Employee
# Create your views here.
from newapp import forms

def index(request):
    return render(request,"newapp/index.html")

def empreg(request):
    emp=forms.Employee()
    if request.method =='POST':
        form=forms.Employee(request.POST)
        if form.is_valid():
            enam=form.cleaned_data["Empname"]
            des=form.cleaned_data["desig"]
            sa=form.cleaned_data["sal"]
        obj=Employee(Emp_Name=enam,Designation=des,Salary=sa)
        obj.save()
        messages.success(request,"Your Data was added Sucessfully")

    return render(request,"newapp/emp.html",{"emp":emp})