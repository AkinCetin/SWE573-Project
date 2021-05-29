from django.urls import path
from account.views import logoutView
from account.views import changepassword
from account.views import profilesettings
from account.views import createnewuser
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name= 'login'),
    path('logoutView', logoutView, name='logout'),
    path('changepassword', changepassword, name='changepassword'),
    path('profilesettings', profilesettings, name='profilesettings'),
    path('createaccount', createnewuser, name='createaccount'),


]