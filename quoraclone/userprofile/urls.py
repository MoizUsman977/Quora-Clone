from django.urls import path
from userprofile.views import UserProfile, UserAnswers, ProfileData, UserQuestions, UserTopics, UserUpdateView

urlpatterns = [
    path('user-profile/', UserProfile.as_view() , name='user-profile'),
    path('user-profile/profile', ProfileData.as_view() , name='profile'),
    path('user-profile/edit-profile', UserUpdateView.as_view() , name='editUser'),
    path('user-profile/answers', UserAnswers.as_view() , name='answers'),
    path('user-profile/questions', UserQuestions.as_view() , name='questions'),
    path('user-profile/topics', UserTopics.as_view() , name='usertopics'),
]
