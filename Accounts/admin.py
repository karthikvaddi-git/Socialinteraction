from django.contrib import admin


# Register your models here.

from .models import *

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(userprofile)
admin.site.register(fundraiser)

