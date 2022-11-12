from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'slug', 'description', 'price', 'images', 'is_available', 'category')
    prepopulated_fiels = {'slug': ('car_name')}

admin.site.register(Car, CarAdmin)

