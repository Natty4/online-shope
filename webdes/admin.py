from django.contrib import admin
from .models import Chief_of_staff, Aboutus

# Register your models here.

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
	pass

@admin.register(Chief_of_staff)
class Chief_of_staffAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'contact', 'hobby','pictur']