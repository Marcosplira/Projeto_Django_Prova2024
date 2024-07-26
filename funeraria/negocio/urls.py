from django.urls import path
from . import views

urlpatterns = [
    path('servicos/joao/pix/', views.servicos_joao_pix, name='servicos_joao_pix'),
    path('servicos/intervalo/', views.servicos_intervalo, name='servicos_intervalo'),
    path('servicos/pix/menos10000/', views.servicos_pix_menor_10000, name='servicos_pix_menor_10000'),
    path('cliente/cemiterio/<str:cemiterio>/', views.cliente_no_cemiterio, name='cliente_no_cemiterio'),
    path('gasto/joao/', views.gasto_joao, name='gasto_joao'),
]