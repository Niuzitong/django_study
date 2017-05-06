# @Author: 牛子铜 <niuzitong>
# @Date:   2017-05-05T20:44:13+08:00
# @Email:  niuzitong@nonobank.com
# @Filename: views.py
# @Last modified by:   niuzitong
# @Last modified time: 2017-05-05T21:38:21+08:00


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  
