from django.test import TestCase
from django.urls import reverse
from authentication.models import User
from topics.models import Topic
from qna.models import Question, Answer, Vote
from authentication.factorymodel import UserFactory
from topics.factorymodel import TopicFactory


class AnswerVoteViewTest(TestCase):
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

    def test_like_answer(self):
        response = self.client.post(reverse('likeanswer', args=[self.answer.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=None, answer=self.answer)
        self.assertTrue(vote.is_like)
        self.assertFalse(vote.is_dislike)

    def test_dislike_answer(self):
        response = self.client.post(reverse('dislikeanswer', args=[self.answer.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=None, answer=self.answer)
        self.assertFalse(vote.is_like)
        self.assertTrue(vote.is_dislike)

    def test_like_answer_existing_vote(self):
        Vote.objects.create(user=self.user, answer=self.answer, is_like=False, is_dislike=True)

        response = self.client.post(reverse('likeanswer', args=[self.answer.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=None, answer=self.answer)
        self.assertTrue(vote.is_like)
        self.assertFalse(vote.is_dislike)

    def test_dislike_answer_existing_vote(self):
        Vote.objects.create(user=self.user, answer=self.answer, is_like=True, is_dislike=False)

        response = self.client.post(reverse('dislikeanswer', args=[self.answer.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        vote = Vote.objects.get(user=self.user, question=None, answer=self.answer)
        self.assertFalse(vote.is_like)
        self.assertTrue(vote.is_dislike)
