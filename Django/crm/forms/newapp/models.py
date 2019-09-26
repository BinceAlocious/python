from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_Name=models.CharField(max_length=150)
    Designation=models.CharField(max_length=150)
    Salary=models.IntegerField()

    def __str__(self):
        return self.Emp_Name