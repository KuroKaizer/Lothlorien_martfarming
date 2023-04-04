from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registro),
    path('login/', views.login)
]