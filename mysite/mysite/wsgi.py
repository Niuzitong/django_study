# @Author: 牛子铜 <niuzitong>
# @Date:   2017-04-29T18:00:39+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: wsgi.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-04-29T21:15:53+08:00


"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
