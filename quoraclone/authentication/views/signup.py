from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from authentication.forms import UserForm

@ensure_csrf_cookie
def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
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
                return redirect('home')
    else:
        form = UserForm()
    return render(request, 'sign-up.html', {'form': form})