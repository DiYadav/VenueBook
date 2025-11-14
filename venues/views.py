from django.shortcuts import render
from django.shortcuts import redirect


def Home(request):
    return render(request,'home.html')


def signup(request):
    return render(request,'Signup.html')