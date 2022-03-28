from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import loginForm, RegisterForm
from django.contrib import messages



def signUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.info(request, f'form is not valid')
            return redirect('signUp')
    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'dash/register.html', context)


def signIn(request):
    if request.method == 'POST':
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                messages.info(request, f'Usrename or Password is invalid')
                return redirect('login')       
        else:
            messages.info(request, f'Username or Password is not avlid')
            return redirect('login')
    form = loginForm()
    context = {
        'form':form
    }
    return render(request, 'dash/login.html', context)


def signOut(request):
    logout(request)
    return redirect('login')
            