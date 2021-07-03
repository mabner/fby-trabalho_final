from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'index.html')


def formas_pagamento(request):
    return HttpResponse("Cadastro de Formas de Pagamento")


def classif_receber(request):
    return HttpResponse("Cadastro de Classificação de Contas a Receber")


def classif_pagar(request):
    return HttpResponse("Cadastro de Classificação de Contas a Pagar")


def pagar(request):
    contas_pagar = ContasPagar.pagar_objects.obter_todas_contas_pagar()
    return render(request, 'contas_pagar.html', {'contas_pagar': contas_pagar})


def receber(request):
    contas_receber = ContasReceber.receber_objects.obter_todas_contas_receber()
    return render(request, 'contas_receber.html', {'contas_receber': contas_receber})


def detalhar_conta_receber(request, idconta):
    detalhe_conta_receber = ContasReceber.receber_objects.obter_detalhes_conta(
        idconta)
    return render(request, 'receber_detalhes.html', {'detalhe_conta_receber': detalhe_conta_receber})
