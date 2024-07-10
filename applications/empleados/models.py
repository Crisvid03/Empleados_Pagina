from django.db import models
#?importar departamentos ya que estan relacionadas
from applications.departamento.models import Departamento
#?Importar la app tercereada 
from ckeditor.fields import RichTextField

#!
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad ', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        
    def __str__(self):
        return self.habilidad




#! Tabla empleados
trabajos = (
        ('0' , 'CONTADOR'),
        ('1' , 'GERENTE'),
        ('2' , 'ECONOMISTA'),
        ('3' , 'PROGRAMADOR'),
        ('4',  'OTRO'),
        ('5',  'ADMINISTRADOR'),
        ('6',  'PSICOLOGO'),
        ('7',  'INGENIER AMBIENTAL')
    )

# Create your models here.
class Empleado(models.Model):
    name = models.CharField("Nombre  ", max_length = 10)
    last_name = models.CharField("Apelido  ", max_length = 11)
    full_name = models.CharField(
        'nombres completos', 
        max_length=150,
        blank = True    
    )
    job = models.CharField( "Labor ", max_length = 1 , choices = trabajos)
    #? estableciendo llave foranea de uno a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #? estableciendo ralacion de muchos a muchos m2m
    avatar = models.ImageField(upload_to = 'empleado', blank='True' , null=True)
    habilidades = models.ManyToManyField(Habilidades)  
    hojaVia = RichTextField(blank=True)
    
    def __str__(self):
        return   self.name + " " + self.last_name + ". " 