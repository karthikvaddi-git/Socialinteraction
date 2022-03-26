from django.db import models
from Accounts.managers import CustomUserManager
from Accounts.models import CustomUser
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin

from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin

from django.utils import timezone
from django.core.validators import RegexValidator
from Accounts.managers import CustomUserManager
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator
# Create your models her


class fundraiser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,related_name='userhost')
    title = models.CharField(max_length=100)
    description = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(1000000000), MinValueValidator(1)]
    )
    amount_received = models.IntegerField(default=0, validators=[MaxValueValidator(1000000000), MinValueValidator(0)])

    @property
    def current_amount(self):
        return self.amount - self.amount_received

    def __str__(self):
        heading = self.title
        return self.title + " recives $" + str(self.current_amount)