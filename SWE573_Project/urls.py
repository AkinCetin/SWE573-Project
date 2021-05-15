from django.urls import path, include
from SWE573_Project.views import contact
from SWE573_Project.views import mainpage


urlpatterns = [
    path('contact', contact),
    path('', mainpage),

]
