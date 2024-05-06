from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form_signup = RegisterForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('genre_liste')
        
    return render(request, 'users/register.html', {'form_signup' : RegisterForm})


def log_in(request):
    if request.method=='POST':
        form_connect = LoginForm(request.POST)
        if form_connect.is_valid():
            username_form = form_connect.cleaned_data['username']
            password_form = form_connect.cleaned_data['password']
            utilisateur = authenticate(request, username=username_form, password=password_form)
            if utilisateur:
                login(request, utilisateur)
                # messages.success(request, f"Bienvenu cher utilisateur {username_form}")

            #return redirect('tournois/tournois_menu')
            return redirect('genre_liste')
        
    return render(request, 'users/login.html', {'form_connect' : LoginForm})


def log_out(request):
    logout(request)
    return redirect('genre_liste')

