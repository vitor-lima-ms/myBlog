from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=[
        ('news', 'News'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('other', 'Other'),
    ], default='other')
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-createdAt',)
    
class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.publication.title}'
    
    class Meta:
        ordering = ('-createdAt',)