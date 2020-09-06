from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register_user(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        login(request, new_user)
        messages.success(request, "Registered successfully!")
        return redirect('index')

    context = {
        'form':form,
    }
    return render(request, 'register.html',context)

def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Username or Password is wrong!')
            return render(request, 'login.html', context)

        messages.success(request, 'Logged in successfully!')
        login(request, user)
        return redirect('index')

    return render(request, 'login.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')
