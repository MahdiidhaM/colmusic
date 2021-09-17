from django import forms
from .models import Blog,User,Comment
from django.contrib.auth.forms import UserCreationForm

class Form_Update(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = "__all__"


class FormSignup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','author','password1','password2']

class FormLoginup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1']

class Profile_Update(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','author','last_name','first_name']

class Form_value(forms.ModelForm):
    def __init__(self,*args,**kwargs):

        user = kwargs.pop('user')
        super(Form_value,self).__init__(*args,**kwargs)
    class Meta:
            model = User
            fields = ['username','email','first_name','last_name','author']

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body','email']
        
class FormCreate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title','Description','Author','Image','File','Time','Category','Boolean']