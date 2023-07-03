from django.test import TestCase
from django.urls import reverse
from authentication.models import User
from qna.models import Question
from qna.forms import QuestionForm
from authentication.factorymodel import UserFactory
from topics.factorymodel import TopicFactory

class AddQuestionViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.topic = TopicFactory(creator=self.user)
        self.client.login(email=self.user.email, password='password')


    def test_add_question(self):
        response = self.client.post(reverse('add_question', args=[self.topic.id]), {
            'question_text': 'Test question'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('topic_questions', args=[self.topic.id]))

        question = Question.objects.latest('id')
        self.assertEqual(question.user, self.user)
        self.assertEqual(question.topic, self.topic)
        self.assertEqual(question.question_text, 'Test question')

    def test_add_question_invalid_form(self):
        response = self.client.post(reverse('add_question', args=[self.topic.id]), {})
        # self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)

    def test_add_question_get(self):
        response = self.client.get(reverse('add_question', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsInstance(form, QuestionForm)
        self.assertEqual(response.context['topic'], self.topic)
        questions = Question.objects.filter(topic=self.topic).order_by('created_at')
        self.assertEqual(response.context['questions'].count(), questions.count())

    def test_add_question_not_authenticated(self):
        self.client.logout()
        response = self.client.post(reverse('add_question', args=[self.topic.id]), {
            'question_text': 'Test question'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + f'?next={reverse("add_question", args=[self.topic.id])}')

    def test_add_question_follow_topic(self):
        # import pdb; pdb.set_trace()
        response = self.client.get(reverse('add_question', args=[self.topic.id]))
        self.assertFalse(response.context['is_following'])
        response = self.client.post(reverse('follow_page', args=[self.topic.id]))
        response = self.client.get(reverse('add_question', args=[self.topic.id]))
