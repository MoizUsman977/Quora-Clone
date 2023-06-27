from authentication.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from topics.models import Topic
from userprofile.mixins.totalcountmixin import TotalCountsMixin

class UserTopics(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-topics.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        user = self.request.user
        topics = Topic.objects.filter(creator = user)
        paginator = Paginator(topics, 5)
        page_number = self.request.GET.get('page')
        topics_obj = paginator.get_page(page_number)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['topics_obj'] = topics_obj
        context['user'] = user
        return context
   
class UnAuthUserTopics(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-topics.html'
    def get_context_data(self, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)  
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        topics = Topic.objects.filter(creator = user)
        paginator = Paginator(topics, 5)
        page_number = self.request.GET.get('page')
        topics_obj = paginator.get_page(page_number)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['topics_obj'] = topics_obj
        context['user'] = user
        return context    
  