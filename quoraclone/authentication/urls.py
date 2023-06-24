from django.urls import path
from .views import signup_user, login_user, logout_view

urlpatterns = [
    path('sign-up', signup_user, name='Sign-Up'),
    path('', login_user, name='login'),
    path('logout', logout_view, name='logout'),
]
