# models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    YEAR_CHOICES = [('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=1, choices=YEAR_CHOICES)
    marital_status = models.BooleanField()
    issue = models.TextField()
    reference = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.course}"