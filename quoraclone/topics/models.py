from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='topic_pictures')

    def __str__(self):
        return self.title