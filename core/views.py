from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def play(request):
    if request.user.is_authenticated:
        return render(request, 'core/play.html')
    else:
        return render(request, 'warnings/avisolog.html')
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request,'social/register.html', context)

def perfil(request):
    return render(request, 'social/perfil.html')
