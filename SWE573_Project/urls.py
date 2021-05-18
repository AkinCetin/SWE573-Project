from django.urls import path, include
from SWE573_Project.views import contact
from SWE573_Project.views import mainpage
from SWE573_Project.views import tag
from SWE573_Project.views import details
from SWE573_Project.views import report


urlpatterns = [
    path('contact', contact),
    path('', mainpage, name = 'homepage'),
    path('tag/<slug:tagSlug>', tag, name='tag'),
    path('details/<slug:slug>', details, name='details'),
    path('report', report, name = 'report'),


]
