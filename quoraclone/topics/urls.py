from django.urls import path
from topics.views import home, create_topic, topic_page, follow_page, like_answer, dislike_answer, like_question, dislike_question

urlpatterns = [
    path('home/', home, name='home'),
    path('home/likeanswer/<int:answer_id>', like_answer, name='likeanswer'),
    path('home/dislikeanswer/<int:answer_id>', dislike_answer, name='dislikeanswer'),
    path('home/likequestion/<int:question_id>', like_question, name='likequestion'),
    path('home/dislikequestion/<int:question_id>', dislike_question, name='dislikequestion'),
    path('topic/<int:topic_id>/', topic_page, name='topic_questions'),
    path('topic/<int:topic_id>/follow-page', follow_page, name='follow_page'),
    path('home/add-topic/', create_topic, name='addtopic'),
]
