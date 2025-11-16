from rest_framework import  serializers

from .models import CustomUser , UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        
        model = CustomUser
        fields = ["id","email","name","password", "role"]
    
    
    def validate(self, data):
        errors = {}
        if not data.get('email'):
            errors['email'] = ['Email field is required']
        if not data.get('password'):
            errors['password'] = ['Passwordhis field is required']
        if not data.get('name'):
            errors['name'] = ['This field is required']
        if data.get('email') and CustomUser.objects.filter(email=data['email']).exists():
            errors['email'] = ['A user with this email already exists']
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
    
    def create(self, validated_data):
        
        name = validated_data.pop("name")
        
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        UserProfile.objects.create(user=user, name=name)
        
        return user  
        
 

    
class UserProfileSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    class Meta:
        
        model = UserProfile
        fields = ["id","user","name","profile_picture"]