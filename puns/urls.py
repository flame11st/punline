from django.conf.urls import url

from . import views

app_name = 'puns'
urlpatterns = [
    url(r'^$', views.get_word, name='word'),
    url(r'^result/$', views.result, name='result'),
]