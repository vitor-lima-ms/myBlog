from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from user.myForms import LoginForm
from user.myForms import RegisterUserForm

# Create your views here.

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('publication:home')
        else:
            messages.success(request, "Invalid username or password!")
            form = LoginForm()
            return render(request, 'userLogin.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'userLogin.html', {'form': form})
    
def userLogout(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('publication:home')

def userRegister(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "User registered successfully!")
            return redirect('publication:home')
        else:
            form = RegisterUserForm(request.POST)
            return render(request, 'userRegister.html', {'form': form})
    else:
        form = RegisterUserForm()   
    return render(request, 'userRegister.html', {'form': form})