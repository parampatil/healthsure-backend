from django.shortcuts import render, redirect
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login,logout


def LOGIN_VIEW(request):

    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, "index.html",{"msg":" data is connectiong"} )
