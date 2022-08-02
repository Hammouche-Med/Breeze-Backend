
from rest_framework import generics
from .models import User
from . import serializers


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer

class UserDeleteView(generics.DestroyAPIView):
   queryset = User.objects.all()
   serializer_class = serializers.UserSerializer

