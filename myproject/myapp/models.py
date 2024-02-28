from django.db import models

# Create your models here.
# models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Add other fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    # Add other fields as needed

class SalaryPrediction(models.Model):
    YearsExperience= models.FloatField()
    Salary = models.FloatField(null=True, blank=True)