from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from qna.models import Question, Vote



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