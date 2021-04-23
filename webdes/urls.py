from django.urls import path
from . import views

app_name = 'webdes'

urlpatterns = [
	path('', views.aboutpage, name='webdes_detail'),
]