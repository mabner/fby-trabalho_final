from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bem vindo ao Contas a Pagar e Receber!")


def formasPagamento(request):
    return HttpResponse("Cadastro de Formas de Pagamento")


def classReceber(request):
    return HttpResponse("Cadastro de Classificação de Contas a Receber")


def classPagar(request):
    return HttpResponse("Cadastro de Classificação de Contas a Pagar")


def pagar(request):
    return HttpResponse("Cadastro de Contas a Pagar")


def receber(request):
    return HttpResponse("Cadastro de Contas a Receber")
