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
)
#? Models
from .models import Empleado
from .forms import EmpleadoForm



# Create your views here.
class InicioEmpleado(TemplateView):
    template_name = "inicio.html"

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 6
    model = Empleado

    def get_queryset(self):
        palabra = self.request.GET.get("kword", '')
        queryset = Empleado.objects.all()
        
        if palabra:
            queryset = queryset.filter(name__icontains=palabra)

        queryset = queryset.order_by('id')
        return queryset

class listByDeparmets(ListView):
    template_name = 'empleados/list_by_deparmets.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['short_name']
        queryset = Empleado.objects.filter(departamento__short_name=area).order_by('id')
        return queryset

class ListEmpleadosAdmin(ListView):
    template_name = 'empleados/admin.html'
    model = Empleado
    context_object_name = 'empleados'
    paginate_by = 5

    def get_queryset(self):
        return Empleado.objects.all().order_by('id')

class ListByKword(ListView):

    template_name = 'empleados/list_by_word.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra = self.request.GET.get("kword" , '' )
        lista = Empleado.objects.filter(
            name__icontains = palabra)
        return lista

class EmpleadoDelete(DeleteView) :
    model =  Empleado
    template_name = 'empleados/delete.html'
    success_url = reverse_lazy('empleados_urls:view_admin')

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_urls:lista')
    
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.name + 'dddd ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView , self).form_valid(form)

class Habilities(ListView):
    template_name = 'empleados/habilities.html'
    context_object_name = 'habilities'
    def get_queryset(self):
        clave = self.request.GET.get('id')
        empleado = Empleado.objects.get(id=clave)
        return empleado.habilidades.all() 

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/empleado_detail.html"

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoUpdate(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = [
        'name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('empleados_urls:view_admin')
    
    def get_queryset(self):
        queryset = Empleado.objects.all().order_by('id')
        return queryset

