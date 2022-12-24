from django.contrib import admin
from . import views
# Register your models here.
from blog.models import Article, Tag, Category


admin.site.register(Tag)
admin.site.register(Category)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'description', 'img',)
