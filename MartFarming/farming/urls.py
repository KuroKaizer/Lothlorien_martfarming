<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubicacion/', views.ubicacion, name='ubicacion')
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubicacion/', views.ubicacion, name='ubicacion')
>>>>>>> 0f31af80fd51b49155b3cbb4f9f4ad95329b6ab7
]