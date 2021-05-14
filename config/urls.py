from django.contrib import admin
from django.urls import path, include
from SWE573_Project.views import contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SWE573_Project.urls'))
]
