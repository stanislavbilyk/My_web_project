from django.http import HttpResponse, HttpRequest
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Topic, Article
from .forms import ArticleForm



# Поздравляю, это ваш первый контроллер, который может принять запрос и отдать ответ с текстом, больше ничего
def main(request) -> HttpResponse:
    topics = Topic.objects.all()
    return render(request, 'main.html', {'topics': topics})

def my_feed(request) -> HttpResponse:
    return render(request, 'my_feed.html')

def main_article_id(request, article_id: int) -> HttpResponse:
    return render(request, 'article_id.html', {
        'article_id' : article_id,
    })


def article_id_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Cтраница, на которой будут отображаться комментарии к статье по id # {article_id}.")


def article_id_update(request, article_id: int) -> HttpResponse:
    return render(request, 'article_id_update.html', {
        'article_id' : article_id,
    })


def article_id_delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес, который мы будем использовать для удаления статьи по id # {article_id}.")


def create(request: HttpRequest) -> HttpResponse:
    return render(request, 'create.html')


def main_topics(request: HttpRequest) -> HttpResponse:
    return render(request, 'topics.html')


def main_topic_id(request: HttpRequest, id: int) -> HttpResponse:
    topics = Topic.objects.all()
    articles = Article.objects.filter(topic__id=id)
    return render(request, 'topic_id.html',{
        'topic_id' : id, 'articles': articles, 'topics': topics
    })

# def topic_detail(request, pk):
#     topic = get_object_or_404(Topic, pk=pk)
#     articles = topic.articles.all()  # Получаем связанные статьи
#     return render(request, 'topic_detail.html', {'topic': topic, 'articles': articles})
#
# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'article_detail.html', {'article': article})


def topic_id_subscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес для подписки на тему c id # {topic_id}")


def topic_id_unsubscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес для отписки от темы c id # {topic_id}")


def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')


def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'register.html')


def set_password(request: HttpRequest) -> HttpResponse:
    return render(request, 'set_password.html')


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Адрес для выхода с сайта.")


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


def regex(request, year, month):
    try:
        year = int(year)
        month = int(month)

        if year < 1900 or year > 9999:
            return HttpResponse("Ошибка: Неверный формат года", status=400)

        if month < 1 or month > 12:
            return HttpResponse("Ошибка: Неверный формат месяца", status=400)

        datetime(year=year, month=month, day=1)

        formatted_month = f"{month:02d}"

        return render(request, 'regex.html',{
        'year' : year,
        'month' : formatted_month,
    })
    except ValueError:
        return HttpResponse("Ошибка: Некорректная дата", status=400)




