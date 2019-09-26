from django.db import models

# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.Course_Name

class Batch(models.Model):
    Select_Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch_Code=models.CharField(max_length=150,unique=True)
    Date=models.DateField()
    def __str__(self):
        return self.Batch_Code
class User(models.Model):
    User_Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=150)
    def __str__(self):
        return self.User_Email
class Register(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.EmailField()
    Verify_Email=models.EmailField()
    Password=models.CharField(max_length=150)
    Select_Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name