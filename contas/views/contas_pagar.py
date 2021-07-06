from contas.models.contas_pagar import ContasPagar
from django.shortcuts import render


def pagar(request):
    contas_pagar = ContasPagar.pagar_objects.obter_todas_contas_pagar()
    return render(request, 'contas_pagar.html', {'contas_pagar': contas_pagar})


def detalhar_conta_pagar(request, idconta):
    detalhe_conta_pagar = ContasPagar.pagar_objects.obter_detalhes_conta(
        idconta)
    return render(request, 'pagar_detalhes.html', {'detalhe_conta_pagar': detalhe_conta_pagar})
