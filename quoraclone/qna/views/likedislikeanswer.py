from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from topics.models import Topic
from qna.models import  Answer, Vote


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
    try:
        vote = Vote.objects.get(user=user, question=None, answer=answer)
        vote.is_like = False
        vote.is_dislike = True
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, answer=answer, is_like=False, is_dislike=True)

    return redirect('home',)