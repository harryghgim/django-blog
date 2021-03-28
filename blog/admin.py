# Register your models here.

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *

class PostAdmin(MarkdownxModelAdmin):
    """
    Markdown class inherited modeladmin
    """
    list_display = ('title', 'get_partial_content',)

    def get_partial_content(self, obj):
        return obj.content[:50]

admin.site.register(Post, PostAdmin)

