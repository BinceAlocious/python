from django.urls import path
from newapp import views
urlpatterns = [
    path("",views.index),
    path("reg",views.empreg)
]
