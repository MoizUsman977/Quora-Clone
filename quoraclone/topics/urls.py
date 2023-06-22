from django.urls import path
from topics.views import home, create_topic, topic_page, follow_page  

urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:topic_id>/', topic_page, name='topic_questions'),
    path('topic/<int:topic_id>/follow-page', follow_page, name='follow_page'),
    path('home/add-topic/', create_topic, name='addtopic'),
]
