from django.shortcuts import render, redirect, get_object_or_404
from qna.forms import QuestionForm
from topics.models import Topic
from qna.models import Question

def add_question(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data["question_text"]
            Question.objects.create(user=request.user, topic=topic, question_text=question_text)
            return redirect('topic_questions', topic_id=topic_id)
    else:
        form = QuestionForm()
    return render(request, 'add-questions.html', {'form': form})