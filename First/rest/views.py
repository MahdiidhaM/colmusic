from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView
from Music.models import Blog,User
from .serializers import Blog_Api,User_Api
from .permissions import UserPermission


class Choose_Api(ListAPIView):                
    queryset = Blog.objects.all()                       
    serializer_class = Blog_Api 
    

class ListUser_Api(ListAPIView):
    queryset = User.objects.all()                       
    serializer_class = User_Api 


class DetailUser_Api(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = User_Api
    permission_classes = (UserPermission,)


class Create_Api(CreateAPIView):
    queryset = Blog.objects.all()                       
    serializer_class = Blog_Api 


class Update_Api(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()              
    serializer_class = Blog_Api


class Detail_Api(RetrieveAPIView):
    queryset = Blog.objects.all()                       
    serializer_class = Blog_Api 


class Delete_Api(RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_Api 
