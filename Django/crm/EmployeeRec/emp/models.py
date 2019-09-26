from django.db import models

# Create your models here.
class Employee(models.Model):
    empname=models.CharField(max_length=150)
    desig=models.CharField(max_length=150)
    sal=models.IntegerField(default=15000)
    def __str__(self):
        return self.empname
