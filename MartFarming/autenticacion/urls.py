from django.urls import path
from . import views
#from .views import Resgistro,login

urlpatterns = [
    #path('', views.Registro, name='Autenticar'),
    path('', views.login, name='Autenticar'),
]