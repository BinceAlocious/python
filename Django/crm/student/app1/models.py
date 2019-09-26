from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=150)
    address=models.TextField()
    gender=models.CharField(max_length=1)
    age=models.IntegerField()
    email=models.EmailField()
    phno=models.IntegerField()

    def __str__(self):
        return self.name