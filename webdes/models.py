from django.db import models

# Create your models here.

class Chief_of_staff(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	role = models.CharField(max_length=200, db_index=True)
	hobby = models.CharField(max_length=200, db_index=True)
	contact = models.CharField(max_length=200, db_index=True)
	facebook = models.CharField(max_length=200, db_index=True)
	twitter = models.CharField(max_length=200, db_index=True)
	instagram = models.CharField(max_length=200, db_index=True)
	pictur = models.ImageField(upload_to='principals/%Y/%m/%d', blank=True)
	active = models.BooleanField(default=False)
	class Meta:
		ordering = ('-role',)
	def __str__(self):
		return self.name

class Aboutus(models.Model):
	title = models.CharField(max_length=200)
	detail = models.TextField(blank=True)

	def __str__(self):
		return self.title
	
