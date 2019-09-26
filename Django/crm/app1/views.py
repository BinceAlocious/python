from django.shortcuts import render
from app1.forms import RegCourse,RegBatch,RegUser,NewUser
from django.http import HttpResponse
from app1.models import Course,Batch,Register,User
# Create your views here.
def index(request):
    # h="<h1>/addcourse for Courses</h1><p><h1>/addbatch for Batch Schedule</h1></p>"
    obj=RegUser()
    re=Register.objects.all()
    dict={"usr":obj}
    if request.method=='POST':
        us=RegUser(request.POST)
        if us.is_valid():
            u=us.cleaned_data["User_Email"]
            p=us.cleaned_data["Password"]
            for i in re:
                if(u==i.Email):
                    if(p==i.Password):
                        dit={"rec":i}
                        return render(request,"app1/userpg.html",dit)
                    else:
                        return HttpResponse("Error Wrong Password")
                else:
                    return HttpResponse("Error Wrong User Email")
    return render(request,"app1/index.html",dict)

def reg(request):
    obj=RegCourse()
    cr=Course.objects.all()
    dict={"reg":obj,"cr":cr}
    if request.method=='POST':
        frm=RegCourse(request.POST)
        if frm.is_valid():
            frm.save(commit=True)
    return render(request,"app1/addcourse.html",dict)
def edit(request):

   return render(request,"app1/edit.html")

def delete(request):

    return render(request,"app1/delete.html")

def batchreg(request):
    obj=RegBatch()
    ba=Batch.objects.all()
    dict={"obj":obj,"ba":ba}
    if request.method=='POST':
        rec=RegBatch(request.POST)
        if rec.is_valid():
            rec.save(commit=True)
    return render(request,"app1/addbatch.html",dict)
def newuser(request):
    obj=NewUser()
    dict={"nusr":obj}
    if request.method=='POST':
        nus=NewUser(request.POST)
        if nus.is_valid():
            nus.save(commit=True)
    return render(request,"app1/register.html",dict)