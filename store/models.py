from django.db import models
from django.urls import reverse
from django.conf import settings
import os


# Create your models here.

STATUS_CHOICES = (('notavailable', 'Notavailable'),('available', 'Available'),)

RATING_CHOICES = ((1, "★☆☆☆☆"), (2, "★★☆☆☆"), (3, "★★★☆☆"), (4, "★★★★☆"), (5, "★★★★★"))

class AvailableManager(models.Manager):
	def get_queryset(self):
		return super(AvailableManager, self).get_queryset() .filter(status='available')

class City(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	active = models.BooleanField(default=True)
	def __str__(self):
		return self.name
	objects = models.Manager() # The default manager.
	available = AvailableManager() # Our custom manager.

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('store:product_list_by_category', args=[self.slug])


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products',	on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, blank=True, null=True)
	status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='notavailable')
	expiredate = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('name', '-created',)
		index_together = (('id', 'slug'),)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('store:product_detail', args=[self.id, self.slug])
	def get_rating_percentage(self):
		return self.rating * 20 if self.rating is not None else None


	objects = models.Manager() # The default manager.
	available = AvailableManager() # Our custom manager.
	



