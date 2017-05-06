# @Author: 牛子铜 <niuzitong>
# @Date:   2017-05-04T22:44:48+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: views.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-05T00:06:42+08:00


from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Category


def index(request):
    category_list = CategEory.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
