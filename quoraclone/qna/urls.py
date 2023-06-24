from django.urls import path
from qna.views import add_question

urlpatterns = [
    path('topic/<int:topic_id>/add-question', add_question, name='add_question'),
]
