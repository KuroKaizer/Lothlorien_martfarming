from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farming.urls')),
    path('home/', include('farming.urls')),
    path('usuario/', include('autenticacion.urls')),   
] 
