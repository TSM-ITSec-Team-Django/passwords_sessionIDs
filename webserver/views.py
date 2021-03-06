from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import Login, Register


def home(request):
    return render(request, './home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Successful login!')
            return render(request, './home.html')
        else:
            messages.info(request, 'Error!')
            return render(request, './login.html', {'form': Login()})
    else:
        return render(request, './login.html', {'form': Login()})


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.info(request, 'Successful Registration!')
            return render(request, './login.html',{'form': Login()})
        except:
            messages.info(request, 'Error!')
            return render(request, './register.html', {'form': Register()})
    else:
        return render(request, './register.html', {'form': Register()})

@login_required(login_url='/login')
def sign_out(request):
    try:
        logout(request)
        messages.info(request, 'Successful Sign out!')
        return render(request, './home.html')
    except:
        messages.info(request, 'Error!')
        return render(request, './home.html')
