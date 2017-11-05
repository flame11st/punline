from django.conf.urls import url

from . import views

app_name = 'puns'
urlpatterns = [
    url(r'^$', views.get_word, name='word'),
    url(r'^res_(?P<input_word>[A-Za-zА-Яа-я]+)/$', views.result, name='result'),
]