from django.urls import path
from authentication.views.login import login_user, logout_view
from django.contrib.auth import views as auth_views
from authentication.views.signup import signup_user


urlpatterns = [
    path('sign-up', signup_user, name='Sign-Up'),
    path('', login_user, name='login'),
    path('logout', logout_view, name='logout'), 
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'password_reset.html'), name='password_reset'),    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_done.html'), name='password_reset_complete'),
]
