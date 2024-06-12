
# from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from .models import Team
from products.models import Product
from datetime import datetime

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_products = Product.objects.order_by('-date_created').filter(is_featured=True)
    all_products = Product.objects.order_by('-date_created')
    # search_fields = Product.objects.values('model', 'city', 'year', 'body_style')
    brand_search = Product.objects.values_list('brand', flat=True).distinct
    model_search = Product.objects.values_list('model', flat=True).distinct
    city_search = Product.objects.values_list('city', flat=True).distinct
    body_style_search = Product.objects.values_list('body_style', flat=True).distinct
    current_year = datetime.now().year+1
    years = list(range(2000, current_year+1))

    data = {
        'teams': teams,
        'featured_products': featured_products,
        'all_products': all_products,
        'brand_search': brand_search,
        'model_search': model_search,
        'city_search': city_search,
        # 'year_search': year_search,
        'body_style_search': body_style_search,
        'years': years,
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
