from authentication.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from qna.models import Answer
from userprofile.mixins.totalcountmixin import TotalCountsMixin

class UserAnswers(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-answers.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        answers = Answer.objects.filter(user = user).order_by('created_at')
        paginator = Paginator(answers, 5)
        page_number = self.request.GET.get('page')
        answer_obj = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['answer_obj'] = answer_obj
        context['user'] = user
        return context
    
class UnAuthUserAnswers(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-answers.html'
    def get_context_data(self, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)    
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        answers = Answer.objects.filter(user = user)
        paginator = Paginator(answers, 5)
        page_number = self.request.GET.get('page')
        answer_obj = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['answer_obj'] = answer_obj
        context['user'] = user
        return context
  