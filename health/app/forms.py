from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['gender', 'age', 'course', 'year_of_study', 'marital_status', 
                 'issue', 'reference', 'contact']
        widgets = {
            'age': forms.NumberInput(attrs={'min': 18, 'max': 24}),
            'issue': forms.Textarea(attrs={'rows': 4}),
        }