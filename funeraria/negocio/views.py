from django.shortcuts import render
from django.http import HttpResponse
from .models import servicos

def servicos_joao_pix(request):
    servicos = servicos.objects.filter(pagos_com_Pix)
    return HttpResponse(servicos)

def servicos_intervalo(request):
    servicos = servicos.objects.filter(valores__range=(600, 20000))
    return HttpResponse(servicos)

def servicos_pix_menor_10000(request):
    servicos = servicos.objects.filter(valores_menores)
    return HttpResponse(servicos)

def cliente_no_cemiterio(request):
    servicos = Servico.objects.filter(cemiterio=cemiterio)
    return HttpResponse(servicos)

def gasto_joao(request):
    gasto_total = Servico.objects.filter(nome_cliente='João de Deus').aggregate(total=models.Sum('valor_cobrado'))
    return HttpResponse(servicos)