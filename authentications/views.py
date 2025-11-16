from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework import status
from .models import CustomUser, UserProfile
from django.contrib.auth import authenticate
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

@api_view(["POST"])
def register(reuest):
   
   email = reuest.data.get("email")
   
   user = CustomUser.objects.filter(email=email).first()
   
   if user :
      
      return Response({"error":"This Email Already exit"}, status=status.HTTP_400_BAD_REQUEST)
   
   
   serializer = RegisterSerializer(data=reuest.data)
   
   if serializer.is_valid():
      user = serializer.save()
      print("user", user)
      refresh = RefreshToken.for_user(user)
   
      context ={
         "message":"User succesfully registered",
         "access_token" : str(refresh.access_token),
         "refresh_token" : str(refresh),
         "data": serializer.data

      }
      
      return Response(context, status=status.HTTP_201_CREATED)
   
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   
      
@api_view(["POST"])
def login(request):
   
   email = request.data.get("email")
   password = request.data.get("password")
   
   if email is None:
      
      return Response({"error":"Email is required"}, status=400)
   
   if password is None:
      
      return Response({"error":"Password is required"}, status=400)
   
   
   user = authenticate(email=email, password=password)
   
   if user is None:
      
      return Response({"error": "Invlid email or passowrd"}, status=404)
   
   profile = UserProfile.objects.get(user=user)
   refresh = RefreshToken.for_user(user)
   
   serializer = UserProfileSerializer(profile)
   
   context = {
      "accees_token": str(refresh.access_token),
      "refresh_token": str(refresh),
      "profile": serializer.data
      
   }
   
   return Response(context, status=200)



class ProfileGenric(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfile
    permission_classes=[IsAuthenticated]
    
class ProfileRetUpDesGenric(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]
    
    
