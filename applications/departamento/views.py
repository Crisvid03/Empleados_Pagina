from django.shortcuts import render
from django.urls import reverse_lazy
#? Vista
from django.views.generic import(
    ListView , 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    FormView,
)
#? Formulario creado
from .forms import DepartamentoUpdate
#
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here.

class ListDep(ListView):
    template_name = "departamento/listdep.html"
    model = Departamento
    context_object_name='departamentos'
    
    def get_queryset(self):
        queryset = Departamento.objects.all().order_by('id')
        return queryset

class NewDepartamento(CreateView):
    model = Departamento
    template_name = "departamento/registro.html"
    fields = ['name' , 'short_name']
    success_url = reverse_lazy('depart_urls:listado')

class UpdateDepartamento(UpdateView):
    template_name = "departamento/update.html"
    model = Departamento
    form_class = DepartamentoUpdate
    success_url = reverse_lazy('depart_urls:listado')

    def get_queryset(self):
        queryset = Departamento.objects.all().order_by('id')
        return queryset

     
