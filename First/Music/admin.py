from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Blog,IpAdress,Comment
from .form import Blog
from django.contrib.auth.admin import UserAdmin

# admin.site.register(User,UserAdmin)
# admin.site.register(Blog)
admin.site.register(IpAdress)
admin.site.register(Comment)

UserAdmin.fieldsets += ('bolean', {'fields': (['author'])}),
 
@admin.register(Blog)
class BlogList(admin.ModelAdmin):
    list_display=['Title','Category']
@admin.register(User)
class Admin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name','author' ,'is_staff']
    


