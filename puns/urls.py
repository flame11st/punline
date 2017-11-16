from django.conf.urls import url

from . import views

app_name = 'puns'
urlpatterns = [
    url(r'^$', views.get_word, name='word'),
    url(r'^res_(?P<comb>[a-z])_(?P<input_word>[A-Za-z1-9]+)/$', views.result_en, name='result_en'),
    url(r'^res_(?P<comb>[a-z])_(?P<input_word>[А-Яа-я1-9]+)/$', views.result_ru, name='result_ru'),
]