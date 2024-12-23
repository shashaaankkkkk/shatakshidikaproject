# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    return render(request,"index.html")
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change to your home page url name
    else:
        form = UserCreationForm()
    return render(request, 'auth.html', {'form': form, 'isLogin': False})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change to your home page url name
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form': form, 'isLogin': True})

from django.shortcuts import render, redirect
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'quiz.html', {'form': form})

def success(request):
    return render(request, 'sucess.html')