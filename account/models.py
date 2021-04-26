from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

class User(AbstractUser):
    """User model."""

    username = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'(0)+[0-9]{9}', message="Phone number must be entered in the format: '09123.....'. Up to 10 digits allowed.")
    phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=10, unique=True) # validators should be a list

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()

    def get_profile_url(self):
        return reverse('profile',kwargs={'pk':self.pk})
        # return reverse('profile',kwargs={'user':self.user.username,'pk':self.pk})

    def __str__(self):
        return f'@{self.username}'


class Profile(models.Model):
	
    SEX_CHOICE = {('M','Male'),('F','Female')}
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Pro-img/%y%m%d', blank=True,null=True)
    sex = models.CharField(choices=SEX_CHOICE, blank=True,null=True, max_length=1)
    birth_day = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return f'{self.user.email}'
    def first_name(self):
        return f'{self.user.first_name}'
    @property
    def username(self):
        return f'@{self.user.username}'
    @property
    def is_active(self):
        return f'{self.user.is_active}'

    def __str__(self):
        return f'{self.user.username}'
