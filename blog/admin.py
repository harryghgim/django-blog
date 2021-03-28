# Register your models here.

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Image

class ImageInline(admin.TabularInline):
    model = Image

class PostAdmin(MarkdownxModelAdmin):
    """
    Markdown class inherited modeladmin
    """
    inlines = [ ImageInline, ]
    list_display = ('title', 'get_partial_content',)

    def get_partial_content(self, obj):
        return obj.content[:50]

admin.site.register(Post, PostAdmin)

