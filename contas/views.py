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
    return HttpResponse("Cadastro de Contas a Pagar")


def receber(request):
    return HttpResponse("Cadastro de Contas a Receber")


def detalhar_conta_receber(request, idconta):
    conta = ContasReceber.receber_objects.obter_detalhes_conta(idconta)
    dados = {'conta': conta, 'msg': "Conta a receber"}
    return render(request, 'contas/receber_detalhes.html', dados)
