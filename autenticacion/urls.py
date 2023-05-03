from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registro, name="registrar"),
    path('login/', views.LoginFormView.as_view(), name="login")
]