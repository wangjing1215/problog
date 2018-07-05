# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id',
                  'username',
                  'email',
                  'is_staff',
                  )