from rest_framework import routers, serializers, viewsets
from Music.models import User,Blog

class Blog_Api(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class User_Api(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','author']

