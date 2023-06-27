from authentication.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.mixins.totalcountmixin import TotalCountsMixin

class UnAuthProfileData(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['user'] = user
        return context
