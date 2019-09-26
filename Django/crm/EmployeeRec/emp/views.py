from django.shortcuts import render
from emp.models import Employee
# Create your views here.
def index(request):
    data=Employee.objects.order_by("sal")
    dict={"Emprec":data}
    return render(request,"emp/index.html",dict)
