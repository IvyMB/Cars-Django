from django.contrib import admin

from cars.models import Car, Brand
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'value')
    list_filter = ('brand', 'model')
    search_fields = ('id', 'model', 'brand')
    

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)