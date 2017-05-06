# @Author: 牛子铜 <niuzitong>
# @Date:   2017-05-04T22:56:56+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: urls.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-04T23:33:35+08:00


from django.conf.urls import url

from rango import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^about/$', views.about, name='about')]
