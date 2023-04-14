from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farming.urls')),
    path('home/', include('farming.urls')),
    path('usuario/', include('autenticacion.urls')),   
]
