from django.urls import path
from userprofile.views import UserProfile, UserAnswers, ProfileData, UserQuestions, UserTopics, UserUpdateView, UnAuthUserProfile, UnAuthProfileData, UnAuthUserAnswers, UnAuthUserTopics, UnAuthUserQuestions

urlpatterns = [
    path('user-profile/', UserProfile.as_view() , name='user-profile'),
    path('user-profile/profile', ProfileData.as_view() , name='profile'),
    path('user-profile/edit-profile', UserUpdateView.as_view() , name='editUser'),
    path('user-profile/answers', UserAnswers.as_view() , name='answers'),
    path('user-profile/questions', UserQuestions.as_view() , name='questions'),
    path('user-profile/topics', UserTopics.as_view() , name='usertopics'),
    path('user-profile/<int:user_id>', UnAuthUserProfile.as_view() , name='unauth-user-profile'),
    path('user-profile/<int:user_id>/profile', UnAuthProfileData.as_view() , name='unauth-profile'),
    path('user-profile/<int:user_id>/answers', UnAuthUserAnswers.as_view() , name='unauth-answers'),
    path('user-profile/<int:user_id>/questions', UnAuthUserQuestions.as_view() , name='unauth-questions'),
    path('user-profile/<int:user_id>/topics', UnAuthUserTopics.as_view() , name='unauth-usertopics'),
]
