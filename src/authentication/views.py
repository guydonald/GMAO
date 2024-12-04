from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import RegisterUser, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth
from .utils import user_in_group

# Create your views here.

def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Utilisateur creer avec success")
            return redirect('register')
    return render(request, 'authentication/register.html', context={'form': form})

def login_user(request):
    form = LoginForm()
    group_name = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role.name == 'Maintenance':
                messages.success(request, 'Bienvenue sur la plateforme de la maintenance ' +username +' ..!')
                return redirect('maintenance')
            elif user.role.name == 'Production':
                messages.success(request, 'Bienvenue sur la plateforme de la maintenance ' +username +' ..!')
                return redirect('production')
            elif user.role.name == 'Administration':
                messages.success(request, 'Bienvenue sur la plateforme de la maintenance ' +username +' ..!')
                return redirect('maintenance')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'authentication/login.html', context={'form': form})

def home(request):
    return render(request, 'accueil.html')