from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    profile_picture = serializers.ImageFielde()
    class Meta : 
        model = Student
        fields = ["first_name", "last_name", "phone_number", "email", "password", "profile_picture", "roll_no", "course"]
        
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone_number = validated_data.pop('phone_number')
        profile_picture = validated_data.pop('profile_picture')
        roll_no = validated_data.pop('roll_no')
        course = validated_data.pop('course')
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=roll_no,
            role=validated_data.get('role', 'student')
        )
        
        profile= UserProfile.objects.create(
           user = User,
           first_name = first_name,
           last_name = last_name,
           phone_number=phone_number,
           profile_picture=profile_picture
       )
        student = Student.objects.create(user=profile, roll_no=roll_no, course=course)
        return student