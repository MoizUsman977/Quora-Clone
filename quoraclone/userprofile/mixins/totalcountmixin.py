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
