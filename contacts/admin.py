from django.contrib import admin

from pages import models
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'title', 'state', 'city', 'date_created')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'title')
    # list_filter = ('city', 'body_style', 'fuel_type', 'color')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)