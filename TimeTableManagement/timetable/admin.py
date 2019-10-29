from django.contrib import admin
from timetable.models import ClassRoom,Course,Batch,TimeTable
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(ClassRoom)
admin.site.register(TimeTable)
