from django.contrib import admin
from django.urls import path, include
from Accounts import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', views.UserRegistration.as_view(), name='signup'),
    path('login', views.login, name='user_login'),

    path('', views.home, name='home'),
    path('logout', views.logoutuser, name='logout'),    
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('profilecreate/',views.profilecreate,name='profilecreate'),


    path('logout', views.logoutuser, name='logout'),    
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('intrest', views.addintrest, name='addintrest'),

    
    

    
    #Forgot password
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html", success_url = reverse_lazy("password_reset_complete")), name="password_reset_confirm"),  # 3
    path('forgot_password/',auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html", success_url = reverse_lazy("password_reset_done"), email_template_name = 'registration/forgot_password_email.html'), name="reset_password"),     # 1
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name="password_reset_done"),    # 2

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name="password_reset_complete"),   # 4
]
 