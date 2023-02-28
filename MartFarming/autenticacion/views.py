from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Registro(request):
    return render(request, 'Usuarios/registro.html')


def login(request):
    return render(request, 'Usuarios/login.html')

"""class Resgistro(View):
    
    def get(self, request):
        return render(request, 'Usuarios/registro.html')

    def post(self, request):
        pass"""
