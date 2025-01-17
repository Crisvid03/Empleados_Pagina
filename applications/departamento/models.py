from django.db import models

# Create your models here.
class Departamento( models.Model ):
    name = models.CharField( 'Nombre', max_length = 50)
    short_name = models.CharField( 'Nombre corto', max_length = 20)
    funcionando = models.BooleanField('Funcionando', default = False)
    
    def __str__(self):
        return   str(self.id) + "  ||   " + self.name 

    def empleados_count(self):
        return self.empleado_set.count()