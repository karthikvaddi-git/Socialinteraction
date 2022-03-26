from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator
# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class Tag(models.Model):
    name=models.CharField(unique=True,max_length=15)

class Groupdata(models.Model):
    groupname=models.CharField(unique=True,max_length=20)
    description=models.CharField(max_length=200)
    image = models.ImageField(default=" ",upload_to='dynamic/img/user_image',validators=[FileExtensionValidator( ['png','jpg'] )])
    admin=models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,related_name="admin")
    tags=models.CharField(max_length=200)
    groupmembers = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="groupmember")

    def __str__(self):
       return self.groupname

