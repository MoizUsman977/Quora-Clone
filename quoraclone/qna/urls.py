from django.urls import path
from qna.views.addquestions import add_question
from qna.views.likedislikeanswer import like_answer, dislike_answer
from qna.views.likedislikequestion import like_question, dislike_question
from qna.views.useranswer import UserAnswers, UnAuthUserAnswers
from qna.views.userquestion import UserQuestions, UnAuthUserQuestions

urlpatterns = [
    path('home/likeanswer/<int:answer_id>', like_answer, name='likeanswer'),
    path('home/dislikeanswer/<int:answer_id>', dislike_answer, name='dislikeanswer'),
    path('home/likequestion/<int:question_id>', like_question, name='likequestion'),
    path('home/dislikequestion/<int:question_id>', dislike_question, name='dislikequestion'),
    path('topic/<int:topic_id>/add-question', add_question, name='add_question'),
    path('user-profile/answers', UserAnswers.as_view() , name='answers'),
    path('user-profile/<int:user_id>/answers', UnAuthUserAnswers.as_view() , name='unauth-answers'),
    path('user-profile/questions', UserQuestions.as_view() , name='questions'),
    path('user-profile/<int:user_id>/questions', UnAuthUserQuestions.as_view() , name='unauth-questions'),
    
]
