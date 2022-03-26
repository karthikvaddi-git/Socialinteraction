from django.shortcuts import render
from Accounts.models import *

# Create your views here.
def show_profile(request):
    x      = userprofile.objects.filter(user=request.user)
    person = userprofile.objects.get(user=request.user)
    return render(request,'showprofile.html', {'person':person,'x':x})