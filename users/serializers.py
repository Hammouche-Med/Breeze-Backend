from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'first_name', 'last_name', 'phone',
                  'password', 'is_superuser', 'is_staff')


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'password', 'password2', 'is_superuser', 'is_staff')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
# # FTP lib

class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_superuser = serializers.BooleanField(required=True)


    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'phone', 'password', 'is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone = validated_data['phone']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.is_superuser = validated_data['is_superuser']  
        instance.save()

        return instance

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'phone', 'password', 'is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def update(self, instance, validated_data):
         
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
