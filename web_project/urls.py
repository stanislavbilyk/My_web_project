"""
URL configuration for web_module1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path, register_converter
from myapp.views import main, my_feed, create, profile, register, set_password, login, logout, regex, FourDigitYearConverter
from django.contrib import admin


register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', main, name = 'main'),
    path('admin/', admin.site.urls),
    path('my-feed', my_feed, name = 'my_feed'),
    path('<int:article_id>/', include('myapp.article_urls')),
    path('create', create, name = 'create'),
    path('topics/', include('myapp.topic_urls'), name = 'topics'),
    path('profile', profile),
    path('register', register, name = 'register'),
    path('set-password', set_password),
    path('login', login, name = 'login'),
    path('logout', logout),
    re_path(
        r"^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$",
        regex),
]
