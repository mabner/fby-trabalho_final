from contas.models.classificacao_recebimento import ClassificacaoReceber
from django.http.request import HttpRequest
from contas.models.forma_pagamento import FormaPagamento
from contas.models.contas_receber import ContasReceber, SIT_ESCOLHA
from django.shortcuts import render


def receber(request):
    contas_receber = ContasReceber.receber_objects.obter_todas_contas_receber()
    return render(request, 'contas_receber.html', {'contas_receber': contas_receber})


def detalhar_conta_receber(request, idconta):
    detalhe_conta_receber = ContasReceber.receber_objects.obter_detalhes_conta(
        idconta)
    return render(request, 'receber_detalhes.html', {'detalhe_conta_receber': detalhe_conta_receber})


def cadastrar_conta_receber(request: HttpRequest):
    classificacao = ClassificacaoReceber.objects.all()

    if request.method == 'GET':

        formapagar = FormaPagamento.objects.all()
        situacao = SIT_ESCOLHA

        return render('contas_pagar.html', {
            'formapagar': formapagar,
            'situacao': situacao,
            'classificacao': classificacao
        })
    else:
        dados = request.POST
        descricao = dados['descricao']
        data_vencimento = dados['data_vencimento']
        data_pagamento = dados['data_pagamento']
        valor = dados['valor']
        classificacao_id = dados['classificacao']
        formapagar = dados['formapagar']
        situacao = dados['situacao']

        classificacao = ClassificacaoReceber.objects.get(id=classificacao_id)

        ContasReceber.objects.create(
            descricao=descricao,
            data_vencimento=data_vencimento,
            data_pagamento=data_pagamento,
            valor=valor,
            classificacao=classificacao,
            formapagar=formapagar,
            situacao=situacao
        )
