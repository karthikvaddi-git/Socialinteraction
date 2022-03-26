from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'index.html')



def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')

    print("TEHR REQUIRED USER")
    print(str(request.user))
    username=str(request.user)



    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages})

def group(request):
    groupobj=Groupdata.objects.all()
    print(groupobj)
    context={'groupobj':groupobj}
    print(groupobj[0].groupname)
    print(groupobj[0].tag)
    print(context)
    print(request.user)
    return render(request,'groupchat.html',context)
