from contas.models import *
from django.http.request import HttpRequest
from django.shortcuts import render


def fluxo_caixa(request: HttpRequest):
    dados = request.POST.get('dados', False)
    inicio_caixa = dados['inicio_caixa']
    data_inicial = dados['data_inicial'].split('-')
    data_final = dados['data_final'].split('-')
    mes_inicio = int(data_inicial[1])
    mes_final = int(data_final[1])
    ano = int(data_inicial[0])
    total_mes = []

    while mes_inicio <= mes_final:
        mes = {
            'mes': mes_inicio,
            'valores_pagar': {
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
            'saldo': float(inicio_caixa) -
            ContasPagar.pagar_objects.obter_total_pagar_mes(
                mes=mes_inicio, ano=ano) +
            ContasReceber.receber_objects.obter_total_receber_mes(
                mes=mes_inicio, ano=ano)
        }
        mes_inicio += 1
        total_mes.append(mes)

        return render(request, 'fluxo.html',
                      {'inicio_caixa': inicio_caixa, 'total_mes': total_mes})
