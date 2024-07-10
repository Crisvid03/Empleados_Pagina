from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main_home.as_view()),
    path('add-home/', views.PruebaCreate.as_view()),
    path('grillas/',views.GrillasEx.as_view()),
]
