from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
# Create your views here.


class LoginFormView(LoginView):
    template_name = "Usuarios/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'SmartFarming | Login'

def registro(request):
    return render(request, "Usuarios/registro.html")


#def login(request):
    return render(request, "Usuarios/login.html")
