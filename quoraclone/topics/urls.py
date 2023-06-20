from django.urls import path
from topics.views import home, create_topic, topic_page   

urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:topic_id>/', topic_page, name='topic_questions'),
    path('home/add-topic/', create_topic, name='addtopic'),
]