from django.contrib import admin
from .models import Student , MentalHealthAssessment , Appointment
admin.site.register([Student,MentalHealthAssessment,Appointment])