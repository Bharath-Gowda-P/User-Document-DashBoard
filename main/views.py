from pydoc import doc
import os
from urllib import response
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Doc
from django.utils.encoding import smart_str


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def user_login(request):
    if request.method == "POST":
        user = request.POST['username']
        pas = request.POST['password']
        user = authenticate(request, username = user, password = pas)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
          messages.error(request, "INVALID CREDENTIALS")
          return redirect('/login')
    return render(request, 'main/login.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username  = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/signup')

        if password != cpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/signup')

        if email in [None, '']:
            messages.error(request, "Email is required")
            return redirect('signup')

        if username in [None, '']:
            messages.error(request, "Username is required")
            return redirect('signup')

        if password in [None, '']:
            messages.error(request, "Password is required")
            return redirect('signup')

        if cpassword in [None, '']:
            messages.error(request, "Password Confirmation is required")
            return redirect('signup')            

        newuser = User.objects.create_user(username, email, password)
        newuser.save()
        
        return redirect('login')
    return render(request, 'main/signup.html')

@login_required(login_url='login')
def home(request):
    data = Doc.objects.all()
    context = {'data': data}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == "POST":
        dname = request.POST['dname']
        dfile = request.FILES['file']
        user = request.user
        newEntry = Doc(docName = dname, docFile = dfile, user = user)
        newEntry.save()
        return redirect('home')
    return render(request, 'main/add.html')


@login_required
def download(request, id):
    obj = Doc.objects.get(id=id)
    filename = obj.docFile.path
    response = FileResponse(open(filename, 'rb'))
    return response

@login_required
def viewdoc(request, id):
    obj = Doc.objects.get(id=id)
    filename = obj.docFile.path
    response = FileResponse(open(filename, 'rb'))
    return response


def logout_view(request):
    logout(request)
    return redirect('/')