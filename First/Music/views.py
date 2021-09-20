from django.core import paginator
from django.shortcuts import render,redirect
from django.utils.regex_helper import contains
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Blog,User,Comment
from django.contrib.auth import login,logout,authenticate
from .mixin import UpdateMixsin,CreateMxsin,ProfileMixin,SpecialMixin
from .form import Profile_Update,Form_value,FormCreate,FormComment
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponse

def index(request):
    return render(request,'Music/index.html')
# class List_Blog(ListView):
#     queryset = Blog.objects.all()
#     paginate_by = 5
#     template_name = 'Music/blog.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['object'] = Blog.objects.all().annotate(count=Count('hit')).order_by('-count')
#         return context

class List_Blog(ListView):
    model=Blog
    paginate_by = 8
    template_name = 'Music/blog.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['main'] = Blog.objects.all().annotate(count=Count('hits')).order_by('-count')[:5]
    #     return context


class Listspecial(ListView):
    queryset = Blog.objects.all()
    template_name='Music/index.html'


class Create_Blog(CreateMxsin,CreateView):
    model = Blog
    template_name = 'Music/Form.html'
    fields = '__all__'



class Update_Blog(UpdateMixsin,UpdateView):
    model = Blog
    template_name = 'Music/update.html'
    fields = '__all__'

def Login(request):
    if request.method == 'POST':
        form_1 = request.POST['user']
        form_2 = request.POST['password']
        result = authenticate(request,username=form_1,password=form_2)
        if result is not None :
            login(request,result)
            return redirect('Music:List_Blog')
        else:
            return redirect('Music:index')
    return render(request,'Music/login.html')

def Logout(request):
    logout(request)
    return redirect('Music:List_Blog')


class AuthorList(ListView):
    template_name = 'Music/author.html'
    paginate_by = 5
    def get_queryset(self):
        return Blog.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Mahdi'] = Blog.objects.filter(Author=1)
        context['Arman'] = Blog.objects.filter(Author=2)
        return context


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .form import FormSignup
# from .tokens import account_activation_token
from django.http import HttpRequest

def signup(request):
    if request.method == 'POST':
        form = FormSignup(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_active = False
            form.save()
            return redirect('Music:login')
    else:
        form = FormSignup()
    return render(request, 'Music/signup.html', {'form': form})

from django.urls.base import reverse_lazy
class UpdateProfile(ProfileMixin,UpdateView):
    model= User
    form_class = Form_value
    template_name = 'Music/profile.html'
    success_url = reverse_lazy('Music:List_Blog')
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kw = super(UpdateProfile,self).get_form_kwargs()
        kw.update({
            'user':self.request.user
        })
        return kw
        
class CategoryView(ListView):
    template_name = 'Music/category.html'
    def get_queryset(self):
        return Blog.objects.all().order_by('-Time')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dep'] = Blog.objects.filter(Category__contains='dep')
        context['deephouse'] = Blog.objects.filter(Category__contains='deephouse')
        return context

# def Look(request):
#     model = Blog.objects.filter(Q(Category__contains='dep') | Q(Category__contains='deephouse')) 
#     return render(request,'Music/category.html',{'model':model})

def Search(request):
    if request.method == "POST":
        search = request.POST['search']
        searches = Blog.objects.filter(Q(Title__icontains=search) | Q(Description__icontains=search))
    return render(request,'Music/search.html',{'search':searches,'text':search})

# class SearchBlog(ListView):
#     template_name = 'Msic/search.html'
#     def get_queryset(self):
#         search = self.request.GET.get('keyword')
#         return Blog.objects.filter(Q(Title__contains=search) | Q(Description__contains=search))
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
def comment(request,pk):
    post = Blog.objects.get(pk=pk)
    comments = post.comment.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = FormComment(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = FormComment()
    ip_address = request.user.ip_address
    if ip_address not in post.hits.all():
        post.hits.add(ip_address)
    context = {
        'post':post,
        'forms':form,
        'new_comment':new_comment,
        'comments':comments,
    }
    template = 'Music/comment.html','Music/index.html'
    if post.Boolean and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Music:error'))
    return render(request,template,context)

def Error(request):
    return render(request,'Music/error.html')