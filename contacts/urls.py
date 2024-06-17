
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
]