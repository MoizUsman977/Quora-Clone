from django.urls import path
from .views import signup_user, user_list, login_user

urlpatterns = [
    path('', signup_user, name='Sign-Up'),
    path('login/', login_user, name='login'),
    path('user-list/', user_list, name='user_list'),
]