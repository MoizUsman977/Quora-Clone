from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Case, When, IntegerField
from topics.models import Topic
from qna.models import Question, Answer
from qna.forms import AnswerForm


@login_required
def home(request):
    topics = Topic.objects.all()
    questions = Question.objects.annotate(
        total_likes=Sum(Case(When(answer__vote__is_like=True, then=1), output_field=IntegerField())),
        total_dislikes=Sum(Case(When(answer__vote__is_dislike=True, then=1), output_field=IntegerField()))
    ).order_by('-total_likes', 'total_dislikes')
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
