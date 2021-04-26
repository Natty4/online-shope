from django.contrib import admin
from.models import Profile, User
import django.apps  
# Register your models here.
models = django.apps.apps.get_models()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['username','first_name','email','is_active']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['is_active','first_name','email']



for model in models:
	try:
		admin.register(model)
	except:
		pass