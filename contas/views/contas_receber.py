from django.http.request import HttpRequest
from django.shortcuts import render

from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.contas_receber import ContasReceber, SIT_ESCOLHA
from contas.models.forma_pagamento import FormaPagamento


def receber(request):
	contas_receber = ContasReceber.receber_objects.obter_todas_contas_receber()
	return render(request, 'contas_receber.html', {'contas_receber': contas_receber})


def detalhar_conta_receber(request, idconta):
	detalhe_conta_receber = ContasReceber.receber_objects.obter_detalhes_conta(
			idconta)
	return render(request, 'receber_detalhes.html', {'detalhe_conta_receber': detalhe_conta_receber})


def cadastrar_conta_receber(request: HttpRequest):
	classificacao = ClassificacaoReceber.classif_receber_objects.obter_classif_contas_receber()
	situacao = SIT_ESCOLHA
	formapagar = FormaPagamento.pagamentos_objects.obter_formas_pagamento()

	if request.method == 'GET':

		return render('contas_receber.html', {'formapagar':    formapagar,
		                                      'situacao':      situacao,
		                                      'classificacao': classificacao
		                                      })
	else:
		dados = request.POST
		_descricao = dados['descricao']
		_data_expectativa = dados['data_expectativa']
		_data_recebimento = dados['data_recebimento']
		_valor = dados['valor']
		_classificacao_id = dados['classificacao']
		_formapagar = dados['formapagar']
		_situacao = dados['situacao']
		_classificacao = ClassificacaoReceber.classif_receber_objects.obter_detalhe_classif_recebimento(
				id=_classificacao_id)

		ContasReceber.objects.create(
				descricao=_descricao,
				data_expectativa=_data_expectativa,
				data_recebimento=_data_recebimento,
				valor=_valor,
				classificacao=_classificacao,
				formapagar=_formapagar,
				situacao=_situacao
				)

		contas_receber = ContasReceber.receber_objects.obter_todas_contas_receber()

		return render(request, 'contas_receber.html', {'contas_receber': contas_receber})
