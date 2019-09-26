from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Text=models.TextField()
