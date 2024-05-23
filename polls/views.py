from django.shortcuts import render # type: ignore

# Create your views here.
# from django.http import HttpResponse # type: ignore


def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
