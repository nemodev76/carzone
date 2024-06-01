from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Product

# Create your views here.
def products(request):
    return render(request, 'products/products.html')

def product_details(request, id):
    aproduct = get_object_or_404(Product, pk=id)

    data = {
        'aproduct': aproduct,
    }

    return render(request, 'products/product_details.html', data)