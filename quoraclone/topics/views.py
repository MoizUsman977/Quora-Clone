from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import TopicForm
from authentication.models import User

@login_required
@ensure_csrf_cookie
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.creator = request.user
            topic.save()
            return redirect('home')
    else:
        form = TopicForm()
    
    return render(request, 'add-topic.html', {'form': form})



@login_required
def home(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})

