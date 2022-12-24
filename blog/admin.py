from django.contrib import admin
from . import views
# Register your models here.
from blog.models import Article,Tag,Category

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)