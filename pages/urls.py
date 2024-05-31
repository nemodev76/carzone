# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)