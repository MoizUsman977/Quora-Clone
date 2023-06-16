from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import User


@login_required
def home(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})