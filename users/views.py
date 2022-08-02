
from rest_framework import generics
from .models import User
from . import serializers
from backend.permissions import IsAdminUser, IsAuthenticated


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    permission_classes = (IsAuthenticated,IsAdminUser)


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer
    permission_classes = (IsAuthenticated,)


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
