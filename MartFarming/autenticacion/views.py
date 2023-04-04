from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def registro(request):
    return render(request, "Usuarios/registro.html")


def login(request):
    return render(request, "Usuarios/login.html")

