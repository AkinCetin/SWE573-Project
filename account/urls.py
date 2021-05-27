from django.urls import path
from account.views import logoutView
from account.views import changepassword
from account.views import profilesettings


urlpatterns = [
    path('logoutView', logoutView, name='logout'),
    path('changepassword', changepassword, name='changepassword'),
    path('profilesettings', profilesettings, name='profilesettings'),

]