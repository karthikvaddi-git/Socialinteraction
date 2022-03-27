from django.shortcuts import render
from Accounts.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def show_profile(request):
    # x = userprofile.objects.filter(user=request.user)
    person = userprofile.objects.get(user=request.user)
    print("the person")

    print(person)




    return render(request,'showprofile.html', {'person':person})