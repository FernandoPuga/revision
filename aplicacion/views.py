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

# __________________________Mixins y Decorators

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request , 'aplicacion/base.html')



# _______________________________________________________________class_views_carpinteros

class CarpinteroList(LoginRequiredMixin, ListView):
    model = Carpinteros

class CarpinteroCreate(LoginRequiredMixin, CreateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('carpinteros')
 
class CarpinteroDetail(LoginRequiredMixin, DetailView):
    model = Carpinteros

class CarpinteroUpdate(LoginRequiredMixin, UpdateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('carpinteros')

class CarpinteroDelete(LoginRequiredMixin, DeleteView):
    model = Carpinteros
    success_url = reverse_lazy('carpinteros')

# _______________________________________________________________carpinteros busqueda por zona

def buscarCarpinterosZona(request):
    return render(request, "carpinteros_list.html")

def buscar2(request):
    if request.GET['zona']:
        zona = request.GET['zona']
        localidad = Carpinteros.objects.filter(localidad__icontains=zona)
        return render(request,
                     "aplicacion/resultadosZona.html",
                     {"zona":zona, "carpinteros_list":localidad})


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
                return render(request, 'aplicacion/base.html', {"mensaje":f"Bienvenido/a {usuario}"})
            else:
                return render(request, 'aplicacion/login.html', {"form":miForm, "mensaje":f"Datos invalidos"})
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
            return render(request, "aplicacion/base.html", {"mensaje":"Gracias por Registrarte"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})    


