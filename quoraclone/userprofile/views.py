from authentication.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from qna.models import Answer, Question
from topics.models import Topic

class UserProfile(TemplateView):
    template_name = 'user-profile.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions = Question.objects.filter(user=user).count()
        total_answers = Answer.objects.filter(user=user).count()
        total_topics = Topic.objects.filter(creator=user).count()
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['user'] = user
        return context
    
class ProfileData(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context

class UserAnswers(TemplateView):
    template_name = 'user-answers.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        answers = Answer.objects.filter(user = user)
        paginator = Paginator(answers, 5)
        page_number = self.request.GET.get('page')
        answer_obj = paginator.get_page(page_number)
        context['answer_obj'] = answer_obj
        return context
    
class UserQuestions(TemplateView):
    template_name = 'user-questions.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        questions = Question.objects.filter(user = user)
        paginator = Paginator(questions, 5)
        page_number = self.request.GET.get('page')
        questions_obj = paginator.get_page(page_number)
        context['questions_obj'] = questions_obj
        return context
    
class UserTopics(TemplateView):
    template_name = 'user-topics.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        topics = Topic.objects.filter(creator = user)
        paginator = Paginator(topics, 5)
        page_number = self.request.GET.get('page')
        topics_obj = paginator.get_page(page_number)
        context['topics_obj'] = topics_obj
        return context
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'email', 'username', 'age', 'gender', 'profile_picture']
    template_name = 'edit-user-data.html'
    success_url = reverse_lazy('profile') 
    
    def get_object(self, queryset=None):
        return self.request.user
    
