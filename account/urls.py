from django.urls import path, include
from .import views



urlpatterns = [
	 path('', include('django.contrib.auth.urls')),
     path('dashboard/',views.dashboard, name='dashboard'),
     # path('profile/<pk>/',views.profile_view, name='profile'),
     path('register/',views.register, name='register'),
     path('verify/',views.verify_view, name='verify_me'),
     path('edit/',views.edit, name='edit'),
     path('delete/<pk>',views.acc_delete, name='delete_account'),
]