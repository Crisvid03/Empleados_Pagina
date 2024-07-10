from django.contrib import admin
from django.urls import path

from . import views



app_name= "depart_urls"


urlpatterns = [
    path('list-dep/', 
        views.ListDep.as_view(),
        name = 'listado'
    ),
    path('add-dep/',
        views.NewDepartamento.as_view(),
        name = 'agregar'
    ),
    path('custom-dep/<pk>',
        views.UpdateDepartamento.as_view(),
        name = 'custom'
    ),
]