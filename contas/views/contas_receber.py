from django.shortcuts import render
from contas.models import *


def receber(request):
    contas_receber = ContasReceber.receber_objects.obter_todas_contas_receber()
    return render(request, 'contas_receber.html', {'contas_receber': contas_receber})


def detalhar_conta_receber(request, idconta):
    detalhe_conta_receber = ContasReceber.receber_objects.obter_detalhes_conta(
        idconta)
    return render(request, 'receber_detalhes.html', {'detalhe_conta_receber': detalhe_conta_receber})
