from django.shortcuts import render # type: ignore

# Create your views here.
def products(request):
    return render(request, 'products/products.html')