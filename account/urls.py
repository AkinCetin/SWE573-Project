from django.urls import path
from account.views import logoutView
from account.views import changepassword


urlpatterns = [
    path('logoutView', logoutView, name='logout'),
    path('changepassword', changepassword, name='changepassword'),

]