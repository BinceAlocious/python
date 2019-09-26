from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index),
    path("/form",views.form_name_view)
]