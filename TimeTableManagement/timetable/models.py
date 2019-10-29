from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=256,unique=True)
    def __str__(self):
        return self.Course_Name
class Batch(models.Model):
    Batch_Code=models.CharField(max_length=256,unique=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Starting_Date=models.DateField()
    Fees=models.IntegerField()
    Active_Status=models.IntegerField(default=1)
    def __str__(self):
        return self.Batch_Code
class ClassRoom(models.Model):
    Class_Name=models.CharField(max_length=256,unique=True)
    No_of_Students=models.IntegerField()
    def __str__(self):
        return self.Class_Name
def next_day():
    return datetime.now() + timedelta(days=1)
class TimeTable(models.Model):
    Select_Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Start_Time = models.TimeField(default=datetime.now)
    End_Time = models.TimeField()
    Class_Room=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    Date=models.DateField(default=next_day)
