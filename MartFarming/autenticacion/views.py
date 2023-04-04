<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def registro(request):
    return render(request, "Usuarios/registro.html")


def login(request):
    return render(request, "Usuarios/login.html")

=======
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def registro(request):
    return render(request, "Usuarios/registro.html")


def login(request):
    return render(request, "Usuarios/login.html")

>>>>>>> 0f31af80fd51b49155b3cbb4f9f4ad95329b6ab7
