from authentication.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from qna.models import Answer, Question
from topics.models import Topic



class TotalCountsMixin:
    def get_total_counts(self, user):
        if (self.request.user == user):
            isAuthenticatedUser = True
        else:
            isAuthenticatedUser = False         
        total_questions = Question.objects.filter(user=user).count()
        total_answers = Answer.objects.filter(user=user).count()
        total_topics = Topic.objects.filter(creator=user).count()
        return total_questions, total_answers, total_topics, isAuthenticatedUser

    
class UserProfile(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-profile.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['user'] = user
        return context
    

class UnAuthUserProfile(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-profile.html'
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


class ProfileData(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['user'] = user
        return context

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



class UserAnswers(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-answers.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
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
    
class UserQuestions(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-questions.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        user = self.request.user
        questions = Question.objects.filter(user = user)
        paginator = Paginator(questions, 5)
        page_number = self.request.GET.get('page')
        questions_obj = paginator.get_page(page_number)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['questions_obj'] = questions_obj
        context['user'] = user
        return context

class UnAuthUserQuestions(LoginRequiredMixin, TemplateView, TotalCountsMixin):
    template_name = 'user-questions.html'
    def get_context_data(self, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        total_questions, total_answers, total_topics, isAuthenticatedUser = self.get_total_counts(user)
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(user = user)
        paginator = Paginator(questions, 5)
        page_number = self.request.GET.get('page')
        questions_obj = paginator.get_page(page_number)
        context['total_questions'] = total_questions
        context['total_answers'] = total_answers
        context['total_topics'] = total_topics
        context['isAuthenticatedUser'] = isAuthenticatedUser
        context['questions_obj'] = questions_obj
        context['user'] = user
        return context
    
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
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'email', 'username', 'age', 'gender', 'profile_picture']
    template_name = 'edit-user-data.html'
    success_url = reverse_lazy('profile') 
    
    def get_object(self, queryset=None):
        return self.request.user
