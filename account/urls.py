from django.urls import path
from account.views import logoutView
from account.views import changepassword
from account.views import profilesettings
from account.views import createnewuser


urlpatterns = [
    path('logoutView', logoutView, name='logout'),
    path('changepassword', changepassword, name='changepassword'),
    path('profilesettings', profilesettings, name='profilesettings'),
    path('createaccount', createnewuser, name='createaccount'),


]