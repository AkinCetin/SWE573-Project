from django.urls import path, include
from SWE573_Project.views import mainpage
from SWE573_Project.views import tag
from SWE573_Project.views import details
from SWE573_Project.views import report
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name= 'login'),
    path('aboutus', TemplateView.as_view(
        template_name='pages/aboutus.html'
    ), name = 'aboutus'),
    path('homepage', mainpage, name = 'homepage'),
    path('tag/<int:article_id>', tag, name='tag'),
    path('details/<slug:slug>', details, name='details'),
    path('report/<int:article_id>', report, name = 'report'),



]
