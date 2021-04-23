from django.urls import path
from . import views

app_name = 'store'


urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('search/', views.product_search, name='search'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

	]