# from Music.models import Comment
from django.urls import path
from django.urls.conf import re_path
from .views import *

app_name='Music'

urlpatterns = [
    path('',Listspecial.as_view(),name='index'),
    path('blog/',List_Blog.as_view(),name='List_Blog'),
    path('create/',Create_Blog.as_view(),name='create'),
    path('update/<int:pk>',Update_Blog.as_view(),name='update'),
    # path('update_def/',update,name='update_def'),
    path('error/',Error,name='error'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('blog/Mahdi/',AuthorList.as_view(),name='Author'),
    path('blog/Arman/',AuthorList.as_view(),name='Author'),
    path('signup/', signup, name='signup'),
    path('profile/', UpdateProfile.as_view(), name='profile'),
    path('blog/dep/',CategoryView.as_view(),name='dep'),
    path('blog/deephouse/',CategoryView.as_view(),name='deephouse'),
    path('search/',Search,name='search'),
    path('comment/<int:pk>',comment,name='comment'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
]
