
from django.contrib import admin # type: ignore

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


# admin.site.register(UserAdmin)