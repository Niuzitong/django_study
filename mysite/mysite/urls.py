# @Author: 牛子铜 <niuzitong>
# @Date:   2017-04-29T18:00:39+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: urls.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-04-29T18:48:59+08:00


"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^pools/', include('pools.urls')),
    url(r'^admin/', admin.site.urls),
]
