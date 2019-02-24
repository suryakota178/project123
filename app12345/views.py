from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DetailView,DeleteView
from django.contrib.auth.models import User
from app12345.forms import Form1,Form2
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from app12345.models import Actor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from app12345.forms import ActorForm
'''
class List(ListView):
    template_name = 'list.html'
    model = Actor
   
def query1(request):
query=request.GET.get('q')
if query:
queryset_list= queryset_list.filter
            
'''



def list(request):
    query=request.GET.get('q',None)
    qs=Actor.objects.all()
    if query is not None:
        qs=qs.filter(
            Q(name__icontains=query)|
            Q(movie__icontains=query)|
            Q(age__icontains=query) |
            Q(about__icontains=query)
        )
    context={
        'object_list':qs
    }

    return render(request, 'list.html', context)


def register(request):
    form1=Form1()
    form2=Form2()
    if request.method=='POST':
        form1=Form1(data=request.POST)
        form2=Form2(data=request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            profile=form2.save()
            profile.user=user
            profile.save()
        else:
            pass
    else:
        pass
    return render(request,'register.html',{'form1':form1,'form2':form2})

def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('app12345:list'))
        else:
            return render(request,'error.html')
    return render(request,'login.html',{})


@login_required
def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('app12345:list'))

def index(request):
    return render(request,'index.html')

class Detail(DetailView):
    model = Actor
    template_name = 'detail.html'


class Create(LoginRequiredMixin,CreateView):
    model = Actor
    template_name = 'create.html'
    fields = ('name','age','movie','about','image')
'''
def create(request):
    form=ActorForm()
    if request.method=="POST":
        form=ActorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        pass
    return render(request,'create.html',{'form':form})

class Update1(LoginRequiredMixin,UpdateView):
    model = Actor
    template_name = 'update.html'
    fields = ('about','age')
'''

class Update(LoginRequiredMixin,UpdateView):
    model = Actor
    template_name = 'create.html'
    fields = ('about','image','age')
    
     #<li class="nav-item">
        #<a class="nav-link " href="{% url 'app12345:create' %}">Create</a>
      #</li>




class Delete(LoginRequiredMixin,DeleteView):
    model = Actor
    template_name = 'delete.html'
    success_url = reverse_lazy('app12345:list')

