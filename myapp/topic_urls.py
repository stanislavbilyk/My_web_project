from django.urls import path
from myapp.views import main_topics, main_topic_id, topic_id_subscribe, topic_id_unsubscribe

urlpatterns = [
    path('', main_topics, name='topics'),
    path('<int:topic_id>/', main_topic_id, name='topic_id'),
    path('<int:topic_id>/subscribe/', topic_id_subscribe, name='topic_id_subscribe'),
    path('<int:topic_id>/unsubscribe/', topic_id_unsubscribe, name='topic_id_unsubscribe'),
]
