from django.contrib import admin
from .models import Category, Product, City
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'rating', 'status', 'created', 'updated']
	list_filter = ['status','rating', 'created', 'updated']
	list_editable = ['price','rating', 'status']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	pass