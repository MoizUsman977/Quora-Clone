from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import TopicForm
from topics.models import Topic
from qna.models import Question, Answer
from qna.forms import AnswerForm

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
    topics = Topic.objects.all()
    questions = Question.objects.all().order_by('-answer__created_at') 
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data["question_id"]
            answer_text = form.cleaned_data["answer_text"]
            question = get_object_or_404(Question, id=question_id)
            Answer.objects.create(user=request.user, question=question, answer_text=answer_text)
            return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'home.html', {'topics': topics, 'questions': questions, 'form': form})

@login_required
def topic_page(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    total_followers = topic.followers.count()
    questions = Question.objects.filter(topic=topic)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data["question_id"]
            answer_text = form.cleaned_data["answer_text"]
            question = get_object_or_404(Question, id=question_id)
            Answer.objects.create(user=request.user, question=question, answer_text=answer_text)
            return redirect('topic_questions', topic_id=topic_id)
    else:
        form = AnswerForm()
    return render(request, 'topic-page.html', {'topic': topic, 'questions': questions, 'form': form, "total_followers":total_followers})

@login_required
def follow_page(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)    
    topic.followers.add(request.user)
    topic.save()
    return redirect('topic_questions', topic_id=topic_id)
