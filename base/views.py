from django.shortcuts import render, redirect
from .forms import BlogAdd, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')        
def blog_add(request):
    form = BlogAdd()
    if request.method == 'POST':
        form = BlogAdd(request.POST,  request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  
            blog.author = request.user      #this is done so that current user who is logged in assigned to the blog he adds
            blog.save() 
            return redirect('home')
        else:
            messages.error(request, "Some error")
    context = {'form': form}
    return render(request, 'base/blogadd.html', context)

def loginUser(request):
    page='login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context= {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    if request.method=='POST':
        if request.POST.get('Logout')=='Logout':
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
    context = {}
    return render(request, 'base/logout.html', context)


def signupUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Some error")
    context={'form': form}
    return render(request, 'base/login_register.html', context)


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    context = {'blogs': blogs}
    return render(request,'base/home.html',context)

def readblog(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog': blog}
    return render(request,'base/readblog.html', context)

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')

# def edit(request, id):
    
