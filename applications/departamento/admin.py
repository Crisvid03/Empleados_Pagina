from django.contrib import admin
from .models import Departamento

# Register your models here.

class DepartAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'short_name', 
        'funcionando',
    )
    
    search_fields = ('short_name',)



admin.site.register(Departamento , DepartAdmin)