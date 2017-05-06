# @Author: 牛子铜 <niuzitong>
# @Date:   2017-05-05T20:51:07+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: serializers.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-05T21:22:57+08:00


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')  
