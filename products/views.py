
from django.shortcuts import render, get_object_or_404 # type: ignore
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator # type: ignore
from datetime import datetime
from .models import Product
from .forms import ProductForm
from .utils import sanitize_html

# Create your views here.
def products(request):
    all_products = Product.objects.order_by('-date_created')
    paginator = Paginator(all_products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    brand_search = Product.objects.values_list('brand', flat=True).distinct
    model_search = Product.objects.values_list('model', flat=True).distinct
    city_search = Product.objects.values_list('city', flat=True).distinct
    # year_search = Product.objects.values_list('year', flat=True).distinct
    body_style_search = Product.objects.values_list('body_style', flat=True).distinct
    first_year = 2000
    current_year = datetime.now().year+1
    years = list(range(first_year, current_year+1))

    data = {
        'all_products': paged_products,
        'brand_search': brand_search,
        'model_search': model_search,
        'city_search': city_search,
        # 'year_search': year_search,
        'body_style_search': body_style_search,
        'years': years,
    }

    return render(request, 'products/products.html', data)
# end products

def product_details(request, id):
    aproduct = get_object_or_404(Product, pk=id)

    data = {
        'aproduct': aproduct,
    }

    return render(request, 'products/product_details.html', data)
# end product_details

def search(request):
    products = Product.objects.order_by('-date_created')
    brand_search = Product.objects.values_list('brand', flat=True).distinct
    model_search = Product.objects.values_list('model', flat=True).distinct
    city_search = Product.objects.values_list('city', flat=True).distinct
    # year_search = Product.objects.values_list('year', flat=True).distinct
    body_style_search = Product.objects.values_list('body_style', flat=True).distinct
    transmission_search = Product.objects.values_list('transmission', flat=True).distinct
    first_year = 2000
    current_year = datetime.now().year+1 # Product.objects.values('year').last()
    years = list(range(first_year, current_year+1))
    min_year = 0
    max_year = 0

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = products.filter(description__icontains=keyword)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            products = products.filter(brand__iexact=brand)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            products = products.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            products = products.filter(city__iexact=city)

    # if 'year' in request.GET:
    #     year = request.GET['year']
    #     if year:
    #         products = products.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            products = products.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            products = products.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price and max_price:
            products = products.filter(price__gte=min_price, price__lte=max_price)

    if 'min_year' in request.GET:
        min_year = request.GET['min_year']

    if not min_year:
        min_year = first_year

    if 'max_year' in request.GET:
        max_year = request.GET['max_year']

    if not max_year:
        max_year = current_year

    products = products.filter(year__gte=min_year, year__lte=max_year)

    data = {
        'products': products,
        'brand_search': brand_search,
        'model_search': model_search,
        'city_search': city_search,
        # 'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
        'years': years,
    }

    return render(request, 'products/search.html', data)
# end search