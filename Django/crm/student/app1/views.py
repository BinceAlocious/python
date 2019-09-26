from django.shortcuts import render

# Create your views here.
from app1.forms import Stuform
from app1.models import Student
def index(request):
    return render(request,"app1/openpg.html")
def reg(request):
    form=Stuform()
    dict={"frm":form}
    if request.method=="POST":
        obj=Stuform(request.POST)
        if obj.is_valid():
            n=obj.cleaned_data["nam"]
            a=obj.cleaned_data["add"]
            g=obj.cleaned_data["gen"]
            ag=obj.cleaned_data["ag"]
            e=obj.cleaned_data["em"]
            p=obj.cleaned_data["ph"]
        #if(int(ag)>18):
            #stu=Student(name=n,address=a,gender=g,age=ag,email=e,phno=p)
            #stu.save()
    return render(request,"app1/index.html",dict)
