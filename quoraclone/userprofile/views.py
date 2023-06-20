from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        print(user)
        for answer in answers:
            print(answer)
        context['user_answers'] = answers
        return context
    
class UserQuestions(TemplateView):
    template_name = 'user-questions.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        questions = Question.objects.filter(user = user)
        print(user)
        for question in questions:
            print(question)
        context['user_questions'] = questions
        return context
    
class UserTopics(TemplateView):
    template_name = 'user-topics.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        topics = Topic.objects.filter(creator = user)
        print(user)
        for topic in topics:
            print(topic)
        context['user_topics'] = topics
        return context
    
