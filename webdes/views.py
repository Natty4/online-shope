from django.shortcuts import render, get_object_or_404
from .models import Chief_of_staff, Aboutus

# Create your views here.

def aboutpage(request):
	cos = Chief_of_staff.objects.filter(active=True)

	abt = get_object_or_404(Aboutus)
	
	return render(request, 'about/about.html', {'cos': cos, 'abt': abt})