#encoding=utf8

from django.conf.urls import url, include
from django.contrib import admin
from . import views


app_name = 'polls'
urlpatterns=[url(r'^$', views.IndexView.as_view(), name='index'),
             url(r'^specifices/(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
             # ex: /polls/5/results/
             url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
             # ex: /polls/5/vote/
             url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
             ]