from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar-mueble/', views.registrar_mueble, name='registrar_mueble'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('resumen-inventario/', views.resumen_inventario, name='resumen_inventario'),
    path('historial-ventas-cliente/<int:cliente_id>/', views.historial_ventas_cliente, name='historial_ventas_cliente'),
    path('perfil-cliente/<int:cliente_id>/', views.perfil_cliente, name='perfil_cliente'),
    path('lista-clientes/', views.lista_clientes, name='lista_clientes'),
]