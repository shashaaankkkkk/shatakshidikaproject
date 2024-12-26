from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentForm, MentalHealthAssessmentForm, AppointmentForm
from .models import Student, MentalHealthAssessment, Appointment
from datetime import datetime, timedelta

from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from django.utils.timezone import now
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form': form, 'isLogin': True})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_form')
    else:
        form = UserCreationForm()
    return render(request, 'auth.html', {'form': form, 'isLogin': False})

@login_required
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('assessment')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
@login_required
def home(request):
    if request.user.is_authenticated:
        try:
            # Fetch the Student instance associated with the logged-in user
            student = Student.objects.get(user=request.user)
            # Fetch upcoming appointments for this student
            upcoming_appointments = Appointment.objects.filter(
                student=student,
                appointment_date__gte=now()
            ).order_by('appointment_date')
        except Student.DoesNotExist:
            # Handle case where no Student is associated with the user
            upcoming_appointments = None
    else:
        upcoming_appointments = None

    return render(request, 'index.html', {'upcoming_appointments': upcoming_appointments})

@login_required
def student_form(request):
    try:
        student = Student.objects.get(user=request.user)
        return redirect('assessment')
    except Student.DoesNotExist:
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.user = request.user
                student.save()
                return redirect('assessment')
        else:
            form = StudentForm()
        return render(request, 'student_form.html', {'form': form})

@login_required
def assessment(request):
    student = get_object_or_404(Student, user=request.user)
    try:
        assessment = MentalHealthAssessment.objects.get(student=student)
        return redirect('schedule_appointment')
    except MentalHealthAssessment.DoesNotExist:
        if request.method == 'POST':
            form = MentalHealthAssessmentForm(request.POST)
            if form.is_valid():
                assessment = form.save(commit=False)
                assessment.student = student
                assessment.save()
                return redirect('schedule_appointment')
        else:
            form = MentalHealthAssessmentForm()
        return render(request, 'assessment.html', {'form': form})

@login_required
def schedule_appointment(request):
    student = get_object_or_404(Student, user=request.user)
    assessment = get_object_or_404(MentalHealthAssessment, student=student)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = student
            appointment.assessment = assessment
            appointment.counselor = assign_counselor()  # You'll need to implement this
            appointment.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('appointment_confirmation')
    else:
        form = AppointmentForm()
    
    # Generate available time slots
    available_slots = generate_time_slots()
    return render(request, 'schedule_appointment.html', {
        'form': form,
        'available_slots': available_slots
    })

@login_required
def appointment_confirmation(request):
    appointment = get_object_or_404(Appointment, student__user=request.user)
    return render(request, 'appointment_confirmation.html', {'appointment': appointment})

def generate_time_slots():
    """Generate available time slots for the next 7 days"""
    slots = []
    start_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    for day in range(7):
        current_date = start_date + timedelta(days=day)
        for hour in range(9, 17):  # 9 AM to 5 PM
            slot_time = current_date.replace(hour=hour)
            slots.append(slot_time)
    return slots

def assign_counselor():
    """Implement counselor assignment logic"""
    # This is a placeholder - you'll need to implement your own logic
    counselors = ['Dr.Shatakshi Singh',"Dr.Anshul Singh Chauhan",'Dr. Ashish Kushwaha',"Dr. Anjali Singh"]
    from random import choice
    return choice(counselors)
def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('home')