from django.urls import path
from .views import home, create_topic   

urlpatterns = [
    path('home/', home, name='home'),
    path('home/add-topic/', create_topic, name='addtopic'),
]