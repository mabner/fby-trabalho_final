from django.http.request import HttpRequest
from django.shortcuts import redirect, render, resolve_url

from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.contas_pagar import ContasPagar, SIT_ESCOLHA
from contas.models.forma_pagamento import FormaPagamento


def pagar(request):
	contas_pagar = ContasPagar.pagar_objects.obter_todas_contas_pagar()
	return render(request, 'contas_pagar.html', {'contas_pagar': contas_pagar})


def detalhar_conta_pagar(request, idconta):
	detalhe_conta_pagar = ContasPagar.pagar_objects.obter_detalhes_conta(
			idconta)
	return render(request, 'pagar_detalhes.html', {'detalhe_conta_pagar': detalhe_conta_pagar})


def cadastrar_conta_pagar(request: HttpRequest):
	if request.method == 'GET':
		# .__str__
		classificacao = ClassificacaoPagar.classif_pagar_objects.obter_classif_contas_pagar()
		formapagar = FormaPagamento.pagamentos_objects.obter_formas_pagamento()
		situacao = SIT_ESCOLHA

		return render('contas_pagar.html', {
				'formapagar':    formapagar,
				'situacao':      situacao,
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

		classificacao = ClassificacaoPagar.objects.get(id=classificacao_id)

		ContasPagar.objects.create(
				descricao=descricao,
				data_vencimento=data_vencimento,
				data_pagamento=data_pagamento,
				valor=valor,
				classificacao=classificacao,
				formapagar=formapagar,
				situacao=situacao
				)

		return redirect(resolve_url('index'))
