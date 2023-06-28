from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import *


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('login')
    
def explore(request):
    return render(request, 'explore.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        concern = request.POST.get('concern')
        contact = Contact(name=name, email=email, phone=phone, concern=concern,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def register(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
    return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=uname, password = pswd)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')
def add_blog(request):
    print(request)
    if request.method == "POST":
        print(request)
        form = BlogForm(request.POST)
        title = request.POST.get('title')
        category = request.POST.get('category')
        user = request.user
        if form.is_valid():
            content = form.cleaned_data['content']
            BlogModel.objects.create(
                user=user,
                title=title,
                content=content,
                category=category,
                pub_date=datetime.today()
            )
            print(content)
            return render(request, 'index.html')
        else:
            context = {
                'form': form,
                'error': "Form is not valid"
            }
            return render(request, 'add_blog.html', context)
    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'add_blog.html', context)
