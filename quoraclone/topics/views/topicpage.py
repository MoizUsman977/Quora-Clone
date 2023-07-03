from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from topics.models import Topic
from qna.models import Question, Answer
from qna.forms import AnswerForm



@login_required
def topic_page(request, topic_id):
    topics = Topic.objects.all()
    user = request.user
    topic = get_object_or_404(Topic, id=topic_id)
    total_followers = topic.followers.count()
    is_following = topic.followers.filter(id=user.id).exists()
    question = Question.objects.filter(topic=topic).order_by('created_at')
    paginator = Paginator(question, 2)
    page_number = request.GET.get('page')
    questions = paginator.get_page(page_number)
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
    return render(request, 'topic-page.html', {'is_following': is_following, 'topics': topics, 'topic': topic, 'questions': questions, 'form': form, "total_followers":total_followers})
