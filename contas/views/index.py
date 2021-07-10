from django.http.request import HttpRequest
from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.forma_pagamento import FormaPagamento
from contas.models.contas_receber import ContasReceber
from contas.models.contas_pagar import ContasPagar
from django.shortcuts import redirect, render


def index(request):
    total = {
        "em_aberto": ContasPagar.pagar_objects.obter_total_em_aberto(),
        "a_receber": ContasReceber.receber_objects.obter_total_a_receber(),
        "saldo": ContasReceber.receber_objects.obter_total_a_receber() - ContasPagar.pagar_objects.obter_total_em_aberto()
    }
    return render(request, 'index.html', {'total': total})


def formas_pagamento(request):
    formas_pagamento = FormaPagamento.pagamentos_objects.obter_formas_pagamento()
    return render(request, 'formas_pagamento.html', {'formas_pagamento': formas_pagamento})


def detalhar_forma_pagamento(request, id):
    detalhe_forma_pagamento = FormaPagamento.pagamentos_objects.obter_detalhe_forma_pagamento(
        id)
    return render(request, 'formas_pag_detalhes.html', {'detalhe_forma_pagamento': detalhe_forma_pagamento})


def cadastrar_formas_pagamento(request: HttpRequest):
    if request.method == 'GET':
        formas_pagamento = FormaPagamento.pagamentos_objects.obter_formas_pagamento()
        return render(request, 'formas_pagamento.html', {'formas_pagamento': formas_pagamento})
    else:
        dados = request.POST
        _descricao = dados['descricao']
        _sigla = dados['sigla']

    pagamento = FormaPagamento(descricao=_descricao, sigla=_sigla)

    pagamento.save()

    formas_pagamento = FormaPagamento.pagamentos_objects.obter_formas_pagamento()

    return render(request, 'formas_pagamento.html', {'formas_pagamento': formas_pagamento})


def apagar_forma_pagamento(resquest, id):
    forma_pag = FormaPagamento.pagamentos_objects.obter_detalhe_forma_pagamento(
        id=id)
    forma_pag.delete()
    return redirect('/formaspagamento')


def classificacao_receber(request):
    classificacao_receber = ClassificacaoReceber.classif_receber_objects.obter_classif_contas_receber()
    return render(request, 'classificacao_receber.html', {'classificacao_receber': classificacao_receber})


def classificacao_pagar(request):
    classificacao_pagar = ClassificacaoPagar.classif_pagar_objects.obter_classif_contas_pagar()
    return render(request, 'classificacao_pagar.html', {'classificacao_pagar': classificacao_pagar})
