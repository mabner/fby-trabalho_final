from django.shortcuts import render
from contas.models import *


def index(request):
    total = {
        "em_aberto": ContasPagar.pagar_objects.obter_total_em_aberto(),
        "a_receber": ContasReceber.receber_objects.obter_total_a_receber(),
    }
    return render(request, 'index.html', {'total': total})


def formas_pagamento(request):
    formas_pagamento = FormaPagamento.objects.all()
    return render(request, 'formas_pagamento.html', {'formas_pagamento': formas_pagamento})


def classif_receber(request):
    classificacao_receber = ClassificacaoReceber.classif_receber_objects.obter_classif_contas_receber(),
    return render(request, 'classificacao_receber.html', {'classificacao_receber': classificacao_receber})


def classif_pagar(request):
    classificacao_pagar = ClassificacaoPagar.classif_pagar_objects.obter_classif_contas_pagar(),
    return render(request, 'classificacao_pagar.html', {'classificacao_pagar': classificacao_pagar})
