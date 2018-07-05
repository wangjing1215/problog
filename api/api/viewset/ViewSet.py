# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import  viewsets
from api.serializers import Serializer
from rest_framework.decorators import detail_route, list_route

class UserViewSet(viewsets.ModelViewSet):
    '''
    王晶
    '''
    queryset = User.objects.all()
    serializer_class = Serializer.UserSerializer

    @list_route(methods=['post'], url_path='changepwd')
    def changepwd(self, request, *args, **kwargs):
        """
        修改密码
        """
        pass