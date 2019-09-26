from django.shortcuts import render
from myapp import forms
from myapp.models import Register
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def form_name_view(request):
    form=forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            nam=form.cleaned_data["name"]
            em=form.cleaned_data["email"]
            tex=form.cleaned_data["text"]
        obj=Register(Name=nam,Email=em,Text=tex)
        obj.save()
        messages.success(request,"Your Data has been Saved")
    return render(request,"myapp/formpage.html",{"form":form})
