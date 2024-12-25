# models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    YEAR_CHOICES = [('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(100)])
    course = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=1, choices=YEAR_CHOICES)
    marital_status = models.BooleanField()
    issue = models.TextField()
    reference = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course}"

class MentalHealthAssessment(models.Model):
    SEVERITY_CHOICES = [
        (1, 'Mild'),
        (2, 'Moderate'),
        (3, 'Severe')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stress_level = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    sleep_issues = models.BooleanField()
    anxiety_level = models.IntegerField(choices=SEVERITY_CHOICES)
    depression_symptoms = models.BooleanField()
    academic_impact = models.IntegerField(choices=SEVERITY_CHOICES)
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment = models.OneToOneField(MentalHealthAssessment, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    counselor = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
