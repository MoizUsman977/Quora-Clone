from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserForm, LoginForm
from .models import User

@ensure_csrf_cookie
def signup_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Create the user
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.set_password(password)  
            user.save() 
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'sign-up.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_list')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})