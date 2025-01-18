from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            # Si la autenticación falla, renderiza la misma página con un mensaje de error
            return render(request, 'authenticate/login.html', {
                'error_message': 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.'
            })
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('landing')

def register(request):
    return render(request, 'authenticate/register.html')