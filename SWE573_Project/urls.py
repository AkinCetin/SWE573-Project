from django.urls import path, include
from SWE573_Project.views import contact
from SWE573_Project.views import mainpage
from SWE573_Project.views import tag
from SWE573_Project.views import details
from SWE573_Project.views import report
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name= 'login'),
    path('contact', contact),
    path('homepage', mainpage, name = 'homepage'),
    path('tag/<slug:tagSlug>', tag, name='tag'),
    path('details/<slug:slug>', details, name='details'),
    path('report/<int:article_id>', report, name = 'report'),


]
