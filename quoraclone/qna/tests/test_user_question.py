from django.test import TestCase, RequestFactory
from django.urls import reverse
from qna.models import Question
from authentication.factorymodel import UserFactory
from topics.factorymodel import TopicFactory


class UserQuestionsViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.topic = TopicFactory(creator=self.user)
        self.question = Question.objects.create(
            user=self.user,
            topic=self.topic,
            question_text='Test question'
        )
        self.client.login(email=self.user.email, password='password')

    def test_user_questions_view(self):
        url = reverse('questions')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-questions.html')
        self.assertEqual(response.context['user'], self.user)

    def test_user_answers_pagination(self):
        # Create multiple Answer objects for pagination
        for i in range(10):
            Question.objects.create(
                user=self.user,
                topic=self.topic,
                question_text=f'Test question? {i}',
            )

        response = self.client.get(reverse('questions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-questions.html')
        self.assertEqual(response.context['user'], self.user)
        questions_obj = response.context['questions_obj']
        self.assertEqual(questions_obj.paginator.num_pages, 3)
