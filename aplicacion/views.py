from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView



# Create your views here.

def index(request):
    return render(request , 'aplicacion/base.html')

def carpinteros(request):
    ctx = {"carpinteros" : Carpinteros.objects.all()}
    return render(request , 'aplicacion/carpinteros.html', ctx)

# _______________________________________________________________class views

class CarpinteroList(ListView):
    model = Carpinteros

class CarpinteroCreate(CreateView):
    model = Carpinteros
    fields = ['nombre', 'apellido', 'email', 'telefono', 'localidad']
    success_url = reverse_lazy('carpinteros')
 
class CarpinteroDetail(DetailView):
    model = Carpinteros
