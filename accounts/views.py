from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('pages:home')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.first_name}! Account created successfully.')
            return redirect('pages:home')
        else:
            # Show exactly what went wrong
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return redirect('pages:home')

    return redirect('pages:home')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('pages:home')

    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
        else:
            messages.error(request, 'Invalid username or password.')
        return redirect('pages:home')  # ← always redirect back to home

    return redirect('pages:home')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('pages:home')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

