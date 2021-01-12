from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

def view1(request):
    if request.method == "GET":
        return render(request, "info.html")


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        User = authenticate(request, username=username, password=password)
        login(request, User)
        if User is not None:

            # return HttpResponse("login successfully")
            return redirect("/info/")
        else:
            return HttpResponse("Check your credentials")


def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        email = request.POST.get("Email")
        password = request.POST.get("password")
        if  User.objects.filter(username=username).exists():
            return HttpResponse("User" + " "+username + "exists Already")
        else:
            user = User.objects.create_user(username, email, password)
            return HttpResponse("Username" + username + "created successfully")


def logoutview(request):
        logout(request)
        return redirect("/info/")
