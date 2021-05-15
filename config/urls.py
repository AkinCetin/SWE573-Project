from django.contrib import admin
from django.urls import path, include
from SWE573_Project.views import contact
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SWE573_Project.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
