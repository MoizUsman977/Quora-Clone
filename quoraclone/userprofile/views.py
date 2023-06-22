from authentication.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from qna.models import Answer, Question
from topics.models import Topic

class UserProfile(TemplateView):
    template_name = 'user-profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'Hello, World!'
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
        context['user_answers'] = answers
        return context
    
class UserQuestions(TemplateView):
    template_name = 'user-questions.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        questions = Question.objects.filter(user = user)
        context['user_questions'] = questions
        return context
    
class UserTopics(TemplateView):
    template_name = 'user-topics.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        topics = Topic.objects.filter(creator = user)
        context['user_topics'] = topics
        return context
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'age', 'gender', 'profile_picture']
    template_name = 'edit-user-data.html'
    success_url = reverse_lazy('profile') 
    
    def get_object(self, queryset=None):
        return self.request.user
    
