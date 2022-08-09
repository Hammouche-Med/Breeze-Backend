from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'first_name', 'last_name',
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

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'password', 'is_superuser', 'is_staff')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})
    #     return attrs

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError(
    #             {"email": "This email is already in use."})
    #     return value


    def update(self, instance, validated_data):
        print(validated_data)
        print(instance)
        instance.username = validated_data['username'],
        instance.email = validated_data['email'],
        instance.first_name = validated_data['first_name'],
        instance.last_name = validated_data['last_name'],
        print("before-*****-----",instance.username[0])
        print(instance.username)
        if validated_data['is_staff'] == 'true' :
            instance.is_staff = True  
        else:
            instance.is_staff = False  
        if validated_data['is_superuser'] == 'true' :
            instance.is_superuser = True  
        else:
            instance.is_superuser = False  
        # instance.is_staff = validated_data['is_staff'],
        # instance.is_superuser = validated_data['is_superuser'],
        print("before------",instance)
        instance.set_password(validated_data['password'])
        instance.save()
        # print("after------",instance)

        return instance
