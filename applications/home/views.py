from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
)
#? Model
from .models import Prueba
from .forms import PruebaForm


# Create your views here.
class main_home(TemplateView):
    template_name = 'home/home.html'
    
    
class PruebaCreate(CreateView):
    template_name = 'home/create.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '/'

class GrillasEx(TemplateView):
    template_name = 'home/grillas.html'