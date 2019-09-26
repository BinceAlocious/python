from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path("",views.index,name='index'),
    path("addcourse",views.reg,name='course'),
    path("edit",views.edit),
    path("delete",views.delete),
    path("addbatch",views.batchreg,name='batch'),
    path("register",views.newuser,name='newusr'),
]
