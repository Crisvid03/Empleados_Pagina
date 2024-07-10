from django.urls import path
from . import views


app_name= "empleados_urls"

urlpatterns = [
    path('',
         views.InicioEmpleado.as_view(),
         name = 'inicio'  
     ),
    path('empleados-total/', 
        views.ListAllEmpleados.as_view(),
        name = 'lista'
    ),
    path('empleados-deparment/<short_name>/', 
        views.listByDeparmets.as_view(),
        name = 'empleados_dep'
    ),
    path('detail-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name = 'detalle'
    ),
    path('empleado-admin', 
        views.ListEmpleadosAdmin.as_view(),
        name = 'view_admin'
    ),
    path('update-empleado/<pk>', 
        views.EmpleadoUpdate.as_view(),
        name = 'update'
    ),
    path('delete-empleado/<pk>', 
        views.EmpleadoDelete.as_view(),
        name = 'delete'
    ),
    path('add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name = 'añadir' 
    ),
    path('habilidades-empleado/', views.Habilities.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
]
