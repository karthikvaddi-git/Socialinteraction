from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')

    print("TEHR REQUIRED USER")
    print(str(request.user))
    username=str(request.user)
    messages = Message.objects.filter(room=room_name)[0:25]
    groupobj=Groupdata.objects.get(groupname=room_name)

    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages,'groupobj':groupobj})

@login_required
def group(request):
    try:
        groupobj = Groupdata.objects.filter(admin=request.user)
        allgroup = Groupdata.objects.all()
        print(groupobj)
        context = {'groupobj': groupobj,'allgroup':allgroup}
        print(context)
        print(request.user)
        return render(request, 'groupinfo.html', context)

    except Groupdata.DoesNotExist:
        context={'groupobj':''}

        return render(request,'groupinfo.html',context)


class creategroup(LoginRequiredMixin,CreateView):
    template_name = 'create_group.html'
    success_url = reverse_lazy('group')
    form_class = groupform
    
    def form_valid(self, form):
        user = self.request.user
        user.save()
        form.instance.groupmembers= user
        form.instance.admin = user
        return super().form_valid(form)




