from django.contrib import admin
from .models import Topic, Article, Comment
# Register your models here.
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comment)
