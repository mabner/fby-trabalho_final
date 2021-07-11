from django.http.request import HttpRequest
from django.shortcuts import render

from contas.models.contas_pagar import ContasPagar
from contas.models.contas_receber import ContasReceber


def fluxo_caixa(request: HttpRequest):
	if request.method == 'GET':
		return render(request, 'fluxo_gerar.html')
	else:
		dados = request.POST
		inicio_caixa = dados['inicio_caixa']
		data_inicial = dados['data_inicial'].split('-')
		data_final = dados['data_final'].split('-')
		mes_inicio = int(data_inicial[1])
		mes_final = int(data_final[1])
		ano = int(data_inicial[0])
		total_mes = []

		while mes_inicio <= mes_final:
			mes = {
					'mes':             mes_inicio,
					'valores_pagar':   {
							'soma_mes':
								ContasPagar.pagar_objects.obter_total_pagar_mes(
										mes=mes_inicio, ano=ano),
							'soma_classificacao':
								ContasPagar.pagar_objects.obter_soma_pagar_classificacoes(
										mes=mes_inicio, ano=ano),
							},
					'valores_receber': {
							'soma_mes':
								ContasReceber.receber_objects.obter_total_receber_mes(
										mes=mes_inicio, ano=ano),
							'soma_classificacao':
								ContasReceber.receber_objects.obter_soma_receber_classificacoes(
										mes=mes_inicio, ano=ano),
							},
					'saldo':           float(inicio_caixa) -
					                   ContasPagar.pagar_objects.obter_total_pagar_mes(
							                   mes=mes_inicio, ano=ano) +
					                   ContasReceber.receber_objects.obter_total_receber_mes(
							                   mes=mes_inicio, ano=ano)
					}
			mes_inicio += 1
			total_mes.append(mes)

		return render(request, 'fluxo.html',
		              {'inicio_caixa': inicio_caixa, 'total_mes': total_mes})


def fluxo_previsto(request: HttpRequest):
	_em_aberto = ContasPagar.pagar_objects.obter_total_em_aberto()
	_a_receber = ContasReceber.receber_objects.obter_total_a_receber()
	_saldo = _a_receber - _em_aberto
	total_previsto = {
			"em_aberto": _em_aberto,
			"a_receber": _a_receber,
			"saldo":     _saldo
			}
	return render(request, 'fluxo_previsto.html', {'total_previsto': total_previsto})


def fluxo_realizado(request: HttpRequest):
	_pagas = ContasPagar.pagar_objects.obter_total_pago()
	_recebidas = ContasReceber.receber_objects.obter_total_recebido()
	_saldo = _recebidas - _pagas

	fluxo_realizado = {
			"pagas":     _pagas,
			"recebidas": _recebidas,
			"saldo":     _saldo
			}
	return render(request, 'fluxo_realizado.html', {'fluxo_realizado': fluxo_realizado})
