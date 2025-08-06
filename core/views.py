
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

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
