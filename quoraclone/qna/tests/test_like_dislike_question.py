from django.test import TestCase
from django.urls import reverse
from authentication.models import User
from topics.models import Topic
from qna.models import Question, Vote
from authentication.factorymodel import UserFactory
from topics.factorymodel import TopicFactory


class QuestionVoteViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.topic = TopicFactory(creator=self.user)
        self.question = Question.objects.create(
            user=self.user,
            topic=self.topic,
            question_text='Test question'
        )
        self.client.login(email=self.user.email, password='password')

    def test_like_question(self):
        response = self.client.post(reverse('likequestion', args=[self.question.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=self.question, answer=None)
        self.assertTrue(vote.is_like)
        self.assertFalse(vote.is_dislike)

    def test_dislike_question(self):
        response = self.client.post(reverse('dislikequestion', args=[self.question.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=self.question, answer=None)
        self.assertFalse(vote.is_like)
        self.assertTrue(vote.is_dislike)

    def test_like_question_existing_vote(self):
        Vote.objects.create(user=self.user, question=self.question, is_like=False, is_dislike=True)

        response = self.client.post(reverse('likequestion', args=[self.question.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=self.question, answer=None)
        self.assertTrue(vote.is_like)
        self.assertFalse(vote.is_dislike)

    def test_dislike_question_existing_vote(self):
        Vote.objects.create(user=self.user, question=self.question, is_like=True, is_dislike=False)

        response = self.client.post(reverse('dislikequestion', args=[self.question.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=self.question, answer=None)
        self.assertFalse(vote.is_like)
        self.assertTrue(vote.is_dislike)
