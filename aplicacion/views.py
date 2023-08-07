from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# ______________________lista, creacion, detalle, actualizacion, borrar

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# __________________________login/registro

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request , 'aplicacion/base.html')

def carpinteros(request):
    ctx = {"carpinteros" : Carpinteros.objects.all()}
    return render(request , 'aplicacion/carpinteros.html', ctx)

# _______________________________________________________________class_views_carpinteros

class CarpinteroList(ListView):
    model = Carpinteros

class CarpinteroCreate(CreateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('carpinteros')
 
class CarpinteroDetail(DetailView):
    model = Carpinteros

class CarpinteroUpdate(UpdateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('carpinteros')

class CarpinteroDelete(DeleteView):
    model = Carpinteros
    success_url = reverse_lazy('carpinteros')

# ________________________________________________________calss_views_electricistas

class ElectricistasList(ListView):
    model = Electricistas

class ElectricistasCreate(CreateView):
    model = Electricistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('electricistas')
 
class ElectricistasDetail(DetailView):
    model = Electricistas

class ElectricistasUpdate(UpdateView):
    model = Electricistas
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('electricistas')

class ElectricistasDelete(DeleteView):
    model = Electricistas
    success_url = reverse_lazy('electricistas')


# _________________________login

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'aplicacion/base.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'aplicacion/login.html', {"mensaje":f"Datos invalidos"})
        else:
            return render(request, 'aplicacion/login.html', { "form":miForm, "mensaje":f"Datos invalidos"})
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})
    

# _________________________register

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})    


