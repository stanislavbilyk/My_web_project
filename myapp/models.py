import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

TOPICS = (
    ('Football', 'Football'),
    ('Boxing', 'Boxing'),
    ('Running', 'Running'),
    ('Team_games', 'Team games'),
    ('Tennis', 'Tennis'),
    ('F1', 'Formula-1'),
    ('Olympic_games', 'Olympic games'),
    ('Winter_sports', 'Winter sports'),
    ('Fitness', 'Fitness'),
    ('Extreme_sports', 'Extreme sports'),
    ('Top_athletes', 'Top athletes'),
)

class Topic(models.Model):
    name = models.CharField(max_length=15, choices=TOPICS, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subscriber = models.ManyToManyField(User, related_name='subscribed_topics', blank=True)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles', null=True)
    topic = models.ManyToManyField(Topic, related_name='articles')
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']





class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)
    comment = models.ForeignKey('myapp.Comment',
                                null=True,
                                blank=True,
                                on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"

