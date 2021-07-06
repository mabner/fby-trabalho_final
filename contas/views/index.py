from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.forma_pagamento import FormaPagamento
from contas.models.contas_receber import ContasReceber
from contas.models.contas_pagar import ContasPagar
from django.shortcuts import render


def index(request):
    total = {
        "em_aberto": ContasPagar.pagar_objects.obter_total_em_aberto(),
        "a_receber": ContasReceber.receber_objects.obter_total_a_receber(),
        "saldo": ContasReceber.receber_objects.obter_total_a_receber() - ContasPagar.pagar_objects.obter_total_em_aberto()
    }
    return render(request, 'index.html', {'total': total})


def formas_pagamento(request):
    formas_pagamento = FormaPagamento.objects.all()
    return render(request, 'formas_pagamento.html', {'formas_pagamento': formas_pagamento})


def classificacao_receber(request):
    classificacao_receber = ClassificacaoReceber.classif_receber_objects.obter_classif_contas_receber()
    return render(request, 'classificacao_receber.html', {'classificacao_receber': classificacao_receber})


def classificacao_pagar(request):
    classificacao_pagar = ClassificacaoPagar.classif_pagar_objects.obter_classif_contas_pagar()
    return render(request, 'classificacao_pagar.html', {'classificacao_pagar': classificacao_pagar})
