
from django.urls import path
from myapp.views import main_article_id, article_id_comment, article_id_update, article_id_delete
from . import views

urlpatterns = [
    path('', main_article_id, name='article_id'),
    path('comment', article_id_comment, name='article_id_comment'),
    path('update', article_id_update, name='article_id_update'),
    path('delete', article_id_delete, name='article_id_delete'),
]
