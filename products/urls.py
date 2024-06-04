from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('cars', views.products, name='products'),
    path('car/id=<int:id>', views.product_details, name='product_details'),
    path('search', views.search, name='search'),
]