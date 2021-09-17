from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

class IpAdress(models.Model):
    ip_address = models.GenericIPAddressField()


class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=45)
    author = models.BooleanField(default=False)
    
    

# class Blog(models.Model):
#     Style = (
#         ('dep','dep'),
#         ('deephouse','deephouse')
#         )
    
#     Title = models.CharField(max_length=30)
#     Description = models.CharField(max_length=50)
#     Author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     Image = models.ImageField(upload_to='music')
#     File = models.FileField(upload_to='file',blank=True)
#     Time = models.DateTimeField(default=timezone.now)
#     Category = models.CharField(choices=Style,max_length=10)
#     Boolean = models.BooleanField(default=False)
    # hits = models.ManyToManyField(IpAdress,through='Article',blank=True,related_name='hits')
    # hits = models.ManyToManyField(IpAdress,through='Article',blank=True,related_name='hits')
    # comments = models.ForeignKey(Comment,on_delete=models.CASCADE)

class Blog(models.Model):
    Style = (
        ('dep','dep'),
        ('deephouse','deephouse')
        )
    
    Title = models.CharField(max_length=30)
    Description = models.CharField(max_length=50)
    Author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Image = models.ImageField(upload_to='music')
    File = models.FileField(upload_to='file')
    Time = models.DateTimeField(default=timezone.now)
    Category = models.CharField(choices=Style,max_length=10)
    Boolean = models.BooleanField(default=False)
    hits = models.ManyToManyField(IpAdress,through='Article',blank=True,related_name='hits')

    def get_absolute_url(self):
        return reverse('Music:List_Blog')

    def __str__(self):
        return self.Title

class Article(models.Model):
    article = ForeignKey(Blog,on_delete=models.CASCADE)
    ip_address = ForeignKey(IpAdress,on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)

    
class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comment')
    name = models.CharField(max_length=200)
    body = models.TextField()
    email = models.EmailField(unique=True,max_length=45)
    create = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)


