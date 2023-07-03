from django.test import TestCase, RequestFactory
from django.urls import reverse
from authentication.models import User
from qna.models import Answer, Question
from topics.models import Topic
from qna.views.useranswer import UserAnswers
from authentication.factorymodel import UserFactory
from topics.factorymodel import TopicFactory


class UserAnswersViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.topic = TopicFactory(creator=self.user)
        self.question = Question.objects.create(
            user=self.user,
            topic=self.topic,
            question_text='Test question'
        )
        self.answer = Answer.objects.create(
            user=self.user,
            question=self.question,
            answer_text='Test answer'
        )
        self.client.login(email=self.user.email, password='password')
        self.url = reverse('answers')

    def test_user_answers_view(self):
        response = self.client.get(reverse('answers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-answers.html')

    def test_user_answers_pagination(self):
        # Create multiple Answer objects for pagination
        for i in range(10):
            Answer.objects.create(
                user=self.user,
                question=self.question,
                answer_text=f'Test answer {i}',
            )

        response = self.client.get(reverse('answers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-answers.html')
        self.assertEqual(response.context['user'], self.user)
        answer_obj = response.context['answer_obj']
        self.assertEqual(answer_obj.paginator.num_pages, 3)
