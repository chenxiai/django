from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


# Register your models here.
admin.site.register(Article, ArticleAdmin)
