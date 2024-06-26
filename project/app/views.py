from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def login(request):
    return render(request, 'app/login.html')


def profile(request):
    return render(request, 'app/profile.html')


def registration(request):
    return render(request, 'app/registration.html')

def registerpage(request):
    return render(request, 'app/registration.html')

def loginpage(request):
    return render(request, 'app/login.html')

def mobile(request):
    return render(request, 'app/mobile.html')
