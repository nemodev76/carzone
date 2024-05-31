from django.contrib import admin # type: ignore
from .models import Car
from django.utils.html import format_html # type: ignore

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width=40 style="border-radius: 50px;"/>'.format(object.car_image.url))
    
    thumbnail.short_description = 'image'

    list_display = ('id', 'thumbnail', 'title', 'city', 'color', 'year', 'body_style', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('id', 'title', 'model', 'city', 'year', 'body_style')
    list_filter = ('city', 'body_style', 'fuel_type', 'color')
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)
