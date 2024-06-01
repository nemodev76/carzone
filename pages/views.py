
# from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from .models import Team
from products.models import Product

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_products = Product.objects.order_by('-date_created').filter(is_featured=True)
    all_products = Product.objects.order_by('-date_created')

    data = {
        'teams': teams,
        'featured_products': featured_products,
        'all_products': all_products,
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
