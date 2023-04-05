from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "farming/index.html")

def ubicacion(request):
    return render(request, "farming/ubicacion.html")
