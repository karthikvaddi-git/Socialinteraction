from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
# ,LoginView
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Accounts.forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from Accounts.forms import *



from socialinteraction import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class UserRegistration(CreateView):
    template_name ='registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/auth/signup/'
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user_email= request.POST.get('email')
        if response.status_code == 302:
            user = CustomUser.objects.get(email=user_email)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your account"
            message =render_to_string('registration/activation_email.html',{
                'user': user,
                'domain': current_site,
                'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
                
            })
            print(message)
            to_email = user_email
            form = self.get_form()
            
            try:
                send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list= [to_email],
                    fail_silently=False,    # if it fails due to some error or email id then it get silenced without affecting others
                )
                messages.success(request, "The link has been sent to your email id to activate your account. please check your inbox and if its not there check your spam as well.")
                return self.render_to_response({'form':form})
            except:
                form.add_error('', 'Error Occured In Sending Mail, Try Again')
                messages.error(request, "Error Occured In Sending Mail, Try Again")
                return self.render_to_response({'form':form})
        else:
            return response
    
    
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist) as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        messages.success(request, "Successfully Logged In")
        return render(request, 'registration/confirmation_success.html')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid or your account is already Verified! Try To Login')
                
        
    
def login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           auth_login(request, user)
           return redirect('/')
       else:
           messages.info(request, 'Username or password are not correct')
    
    context = {}
    return render (request, 'registration/login.html', context)

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('user_login')
    return redirect('/')

def addintrest(request):
    
    return render(request, 'intrestpage.html')

def profile(request):
    if request.method == "POST":
        form = userprofile(request.POST)
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('/')
    else:
        u_form = userprofile(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context )

