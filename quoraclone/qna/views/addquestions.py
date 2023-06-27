from django.shortcuts import render, redirect, get_object_or_404
from topics.models import Topic
from qna.forms import QuestionForm
from qna.models import Question


def add_question(request, topic_id):
    topics = Topic.objects.all()
    user = request.user
    topic = get_object_or_404(Topic, id=topic_id)
    total_followers = topic.followers.count()
    is_following = topic.followers.filter(id=user.id).exists()
    questions = Question.objects.filter(topic=topic)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data["question_text"]
            Question.objects.create(user=request.user, topic=topic, question_text=question_text)
            return redirect('topic_questions', topic_id=topic_id)
    else:
        form = QuestionForm()
    return render(request, 'add-questions.html', {'is_following':is_following, 'topics': topics, 'topic': topic, 'questions': questions, 'form': form, "total_followers":total_followers})