from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def Home(request):
    return render(request,'home.html')