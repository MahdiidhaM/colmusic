from django.urls import path
from .views import Choose_Api,Create_Api,Detail_Api,Update_Api,ListUser_Api,DetailUser_Api,Delete_Api

urlpatterns = [
    path('',Choose_Api.as_view(),name='view'),
    path('create/',Create_Api.as_view(),name='create'),
    path('update/<int:pk>',Update_Api.as_view(),name='update'),
    path('<int:pk>',Detail_Api.as_view(),name='Detail'),
    path('users/',ListUser_Api.as_view(),name='User'),
    path('user/<int:pk>',DetailUser_Api.as_view(),name='User'),
    path('delete/<int:pk>',Delete_Api.as_view(),name='delete'),
]