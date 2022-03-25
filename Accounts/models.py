from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from .models_fields import LowercaseEmailField
from django.utils import timezone
from django.core.validators import RegexValidator
from Accounts.managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email              = LowercaseEmailField(('email adress'),unique=True)
    # phone_no = models.IntegerField(('phone'),unique=True,default="Null")
    is_staff           = models.BooleanField(default=False)
    is_active          = models.BooleanField(default=True)
    date_joined        = models.DateField(default=timezone.now)
    is_customer        = models.BooleanField(default=True)
    is_serviceProvider = models.BooleanField(default=False)
    is_serviceBusiness = models.BooleanField(default=False)
    fields=[email]
    
    USERNAME_FIELD     = 'email'
    EMAIL_FIELD        = 'email'
    phone_regex        = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone              = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()


class userprofile(models.Model):
    user         = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profileimage = models.ImageField(default=" ",upload_to='media/dynamic/img/user_image')
    name   = models.CharField(default=" ",max_length=40)
    description = models.TextField()
    location = models.CharField(default=" ",max_length=150)
    intrests = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    