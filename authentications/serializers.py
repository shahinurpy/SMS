from rest_framework import serializers
from .models import OTP
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import UserProfile
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'user_profile']
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser']
    def get_user_profile(self, obj):
        try:
            profile = obj.user_profile
            return UserGetProfileSerializer(profile).data
        except UserProfile.DoesNotExist:
            return None
        
class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True) 
    last_name  = serializers.CharField(write_only=True)  
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role', 'first_name', 'last_name']
    
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        
        profile= UserProfile.objects.create(
           user = User,
           first_name = first_name,
           last_name = last_name,
           phone_number=phone_number,
           profile_picture=profile_picture
       )
        
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile   
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email', 'otp']
