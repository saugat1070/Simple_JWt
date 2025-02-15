from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Token.models import Student
from Token.serializers import StudentSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Create your views here.
@api_view(['GET'])
def api_root(request,format=None):
    return Response(status=status.HTTP_200_OK)

class StudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        student_record = Student.objects.all()
        serializer = StudentSerializer(student_record,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        database = Student.objects.all()
        serializer = StudentSerializer(database,data = request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)