from django.shortcuts import render

# Create your views here.
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])

def student_list(request):
    if request.method =="GET":
        
        student =  student.objects.all()
        serializer = StudentSerializer( student, many=True)
        
        return Response(serializer.data, status=200)
    
    if request.method =="POST":
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=201)
        
    return Response(serializer.errors, status=400)

