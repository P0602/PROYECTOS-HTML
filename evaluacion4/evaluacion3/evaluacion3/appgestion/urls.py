from django.urls import path
from appgestion import views

urlpatterns = [
    path('', views.index),
    path('ingresar', views.ingresar),
    path('listar', views.listar),
    path('eliminar', views.eliminar),
    path('modificar', views.modificar),
    path('registrar', views.registrar),
    path('listar_despacho',views.listar_despacho),
    path('eliminar_despacho',views.eliminar_despacho),
    path('modificar_despacho', views.modificar_despacho),
    path('filtro', views.filtro),
    path('indicador', views.indicador),
]
