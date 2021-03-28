# core
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# django-taggit
from taggit.managers import TaggableManager

# django-markdownx setting
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

User = get_user_model()

class Post(models.Model):
    """
    posts for author
    """
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) # use my local time as defined in prod_settings.py
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    # reverse instead of redirect
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # markdownify runner 
    # use this method in templates as property of post (Post instance)
    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    class Meta:
        db_table = 'post'