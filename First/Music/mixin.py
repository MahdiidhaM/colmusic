from django.http import Http404,HttpResponseRedirect
from .models import Blog,User
from django.urls import reverse


class UpdateMixsin():
    def dispatch(self,request,pk,*args,**kwargs):
        model = Blog.objects.get(pk=pk)
        if request.user.is_superuser or request.user == model.Author:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404('No Way')

class CreateMxsin():
    def dispatch(self,request,*args,**kwargs):
        # model = User.objects.get(author=True)
        if request.user.is_superuser or request.user.author :
            return super().dispatch(request,*args,**kwargs)
        else:
            return HttpResponseRedirect(reverse('Music:error'))

class ProfileMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        raise Http404('No Way Braw')

class SpecialMixin():
    def dispatch(self,request,**kwargs):
        models = Blog.objects.all()
        for model in models:
            if model.Boolean and not request.user.is_authenticated :
                return HttpResponseRedirect(reverse('Music:error'))
            else :
                return super().dispatch(request,**kwargs)