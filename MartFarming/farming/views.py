<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "farming/index.html")

def ubicacion(request):
    return render(request, "farming/ubicacion.html")
=======
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "farming/index.html")

def ubicacion(request):
    return render(request, "farming/ubicacion.html")
>>>>>>> 0f31af80fd51b49155b3cbb4f9f4ad95329b6ab7
