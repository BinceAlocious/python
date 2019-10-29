from django.urls import path
from timetable import views
app_name='timetable'
urlpatterns = [
    path("home",views.Homepg.as_view(),name='home'),
    path("",views.CreateTable,name='create'),
    path("ajax/getdrop",views.get_room,name='getdrop'),
    path("timetable",views.ViewTimeTable.as_view(),name='view'),
    path("form",views.get_form,name='form'),
    path("endsession",views.endsession,name='end'),
]