from django.urls import path
from SWE573_Project.views import contact


urlpatterns = [
    path('contact', contact),
]
