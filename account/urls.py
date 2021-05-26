from django.urls import path
from account.views import logoutView


urlpatterns = [
    path('logoutView', logoutView, name='logout')
]