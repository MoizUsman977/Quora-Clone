from django.urls import path
from topics.views.createtopic import create_topic
from topics.views.home import home
from topics.views.topicpage import topic_page
from topics.views.followtopic import follow_page
from topics.views.searchtopic import search_topics

urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:topic_id>/', topic_page, name='topic_questions'),
    path('topic/<int:topic_id>/follow-page', follow_page, name='follow_page'),
    path('home/add-topic/', create_topic, name='addtopic'),
    path('search/', search_topics, name='search_topics'),
]
