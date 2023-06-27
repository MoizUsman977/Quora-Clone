from django.urls import path
from userprofile.views.userprofile import UserProfile
from userprofile.views.unauthuserprofile import UnAuthUserProfile
from userprofile.views.profiledata import ProfileData 
from userprofile.views.unauthprofiledata import UnAuthProfileData 
from userprofile.views.usertopics import UserTopics 
from userprofile.views.usertopics import UnAuthUserTopics 
from userprofile.views.userupdateview import UserUpdateView 

urlpatterns = [
    path('user-profile/', UserProfile.as_view() , name='user-profile'),
    path('user-profile/profile', ProfileData.as_view() , name='profile'),
    path('user-profile/edit-profile', UserUpdateView.as_view() , name='editUser'),
    path('user-profile/topics', UserTopics.as_view() , name='usertopics'),
    path('user-profile/<int:user_id>', UnAuthUserProfile.as_view() , name='unauth-user-profile'),
    path('user-profile/<int:user_id>/profile', UnAuthProfileData.as_view() , name='unauth-profile'),
    path('user-profile/<int:user_id>/topics', UnAuthUserTopics.as_view() , name='unauth-usertopics'),
]
