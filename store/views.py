from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import SearchForm
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.available.all()
	cart_product_form = CartAddProductForm()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	paginator = Paginator(products, 6)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		products = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request, 'store/product/list_ajax.html', {'category': category,	'categories': categories, 'products': products, 'cart_product_form': cart_product_form,})
	return render(request, 'store/product/list.html', {'category': category,	'categories': categories, 'products': products, 'cart_product_form': cart_product_form,})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id,	slug=slug, status='available')
	cart_product_form = CartAddProductForm()
	return render(request, 'store/product/detail.html', {'product': product, 'cart_product_form': cart_product_form,})

def product_search(request):
	form = SearchForm()
	query = None
	results = []
	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
		results = Product.available.filter(name__icontains=query,category__name__contains=query,description__contains=query)
	return render(request, 'store/product/search.html', {'form': form, 'query': query, 'results': results})