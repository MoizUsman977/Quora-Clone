from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import TopicForm
from topics.models import Topic
from qna.models import Question, Answer, Vote
from qna.forms import AnswerForm

@login_required
@ensure_csrf_cookie
def create_topic(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.creator = request.user
            topic.save()
            return redirect('home')
    else:
        form = TopicForm()
    
    return render(request, 'add-topic.html', {'form': form, 'topics': topics})



@login_required
def home(request):
    topics = Topic.objects.all()
    questions = Question.objects.all()
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
    topics = Topic.objects.all()
    user = request.user
    topic = get_object_or_404(Topic, id=topic_id)
    total_followers = topic.followers.count()
    is_following = topic.followers.filter(id=user.id).exists()
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
    return render(request, 'topic-page.html', {'is_following':is_following, 'topics': topics, 'topic': topic, 'questions': questions, 'form': form, "total_followers":total_followers})

@login_required
def follow_page(request, topic_id):
    user= request.user
    topic = get_object_or_404(Topic, id=topic_id) 
    is_following = topic.followers.filter(id=user.id).exists()
    if (is_following):
        topic.followers.remove(user)
        topic.save()
    else:
        topic.followers.add(user)
        topic.save()
    return redirect('topic_questions', topic_id=topic_id)

@login_required
def like_answer(request, answer_id):
    user = request.user
    answer = get_object_or_404(Answer, pk=answer_id)
    try:
        vote = Vote.objects.get(user=user, question=None, answer=answer)
        vote.is_like = True
        vote.is_dislike = False
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, answer=answer, is_like=True, is_dislike=False)

    return redirect('home',)

@login_required
def dislike_answer(request, answer_id):
    user = request.user
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question   
    try:
        vote = Vote.objects.get(user=user, question=None, answer=answer)
        vote.is_like = False
        vote.is_dislike = True
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, answer=answer, is_like=False, is_dislike=True)

    return redirect('home',)

@login_required
def like_question(request, question_id):
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote = Vote.objects.get(user=user, question=question, answer=None)
        vote.is_like = True
        vote.is_dislike = False
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, question=question, is_like=True, is_dislike=False)

    return redirect('home',)

@login_required
def dislike_question(request, question_id):
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote = Vote.objects.get(user=user, question=question, answer=None)
        vote.is_like = False
        vote.is_dislike = True
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, question=question, is_like=False, is_dislike=True)

    return redirect('home',)
