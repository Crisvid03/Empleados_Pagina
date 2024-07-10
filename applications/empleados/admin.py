from django.contrib import admin
from  .models import Empleado , Habilidades


admin.site.register(Habilidades)
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display =(
        'id', 
        'name', 
        'last_name',  
        'departamento',
        'job',
        #! Columna creada
        'get_full_name',
    )
    #!Logica rellenar la comlumna
    def get_full_name(self , obj):
        return obj.name + ' ' + obj.last_name
    get_full_name.short_description = 'Nombre Completo'
    
    search_fields = ('name',)
    list_filter = ('job',  'departamento', )
    
    #?Filtro para las habilidades 
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado , EmpleadoAdmin )