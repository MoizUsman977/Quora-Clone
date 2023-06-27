from django.shortcuts import redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from topics.models import Topic




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

