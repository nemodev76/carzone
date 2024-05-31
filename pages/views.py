
# from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from .models import Team
from products.models import Car

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-date_created').filter(is_featured=True)
    all_cars = Car.objects.order_by('-date_created')

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }

    return render(request, 'pages/home.html', data)

def services(request):
    return render(request, 'pages/services.html')

def about(request):
    teams = Team.objects.all()
    
    data = {
        'teams': teams,
    }
    
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
