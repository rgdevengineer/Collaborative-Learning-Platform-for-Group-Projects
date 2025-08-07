
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from .models import StudyGroup
from .forms import StudyGroupForm
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse("Welcome to Collaborative Learning Platform!")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            login(request, user)
            return redirect('home')
        
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required

def create_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            return redirect('home')
    else:
        form = StudyGroupForm()
    return render(request, 'core/create_group.html', {'form': form})

def group_list(request):
    groups = StudyGroup.objects.all().order_by('-created_at')
    return render(request, 'core/group_list.html', {'groups':groups})