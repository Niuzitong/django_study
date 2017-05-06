# @Author: 牛子铜 <niuzitong>
# @Date:   2017-04-29T18:34:06+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: urls.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-04-30T18:27:10+08:00
# coding=utf-8

from django.conf.urls import url
from . import views

app_name='pools'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]
