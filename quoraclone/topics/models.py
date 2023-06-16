from django.db import models
from authentication.models import User

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='topic_pictures')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_topics', null=True)
    followers = models.ManyToManyField(User, related_name='followed_topics')

    def __str__(self):
        return self.title