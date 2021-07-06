# -*- coding: utf-8 -*-
from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.forma_pagamento import FormaPagamento
from django.db import models
from django.db.models import Sum
from django.db.models.deletion import SET_NULL


# Contas a Receber QuerySet
class ReceberQuerySet(models.QuerySet):
    # Query para retornar as contas recebidas
    def contas_recebidas(self):
        return self.filter(situacao="R")

    # Query para retornar os detalhes da conta a receber
    def detalhes_conta(self, idconta):
        return self.filter(id=idconta)

    # Query para retonar as contas não recebidas
    def contas_nao_recebidas(self):
        return self.filter(situacao="N")

    # Query para retornar o valor total das contas a receber
    def total_a_receber(self):
        return float(self.filter(situacao="N").aggregate(
            Sum('valor'))['valor__sum'])

    # Query para retornar o valor total das contas no mês
    def total_receber_mes(self, mes, ano):
        return float(ContasReceber.receber_objects.filter(data_expectativa__month=mes,
                                                          data_expectativa__year=ano)
                     .aggregate(Sum('valor'))['valor__sum'])

    # Query para retonar a soma do mês por classificação
    def soma_receber_mes_classificacao(self, mes, ano):
        classificacoes = ClassificacaoReceber.objects.all().count()
        valores = []

        for class_id in range(1, classificacoes):
            soma_mes_class = float(ContasReceber.receber_objects.filter(data_expectativa__month=mes,
                                                                        data_expectativa__year=ano,
                                                                        classificacao=class_id)
                                   .aggregate(Sum('valor'))['valor__sum'])

        valor = {'classificacao': ClassificacaoReceber.objects.get(id=class_id),
                 'soma_mes_class': soma_mes_class}
        if soma_mes_class > 0:
            valores.append(valor)

        return valores

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(data_expectativa__range=(dataInicio, dataFim))


# Contas a Receber Manager
class ReceberManager(models.Manager):

    def get_queryset(self):
        return ReceberQuerySet(self.model, using=self._db)

    # Retornar todas as contas
    def obter_todas_contas_receber(self):
        return self.all()

    # Retornar a soma das contas em aberto
    def obter_total_a_receber(self):
        return self.get_queryset().total_a_receber()

    # Retornar detalhes da conta
    def obter_detalhes_conta(self, idconta):
        return self.get_queryset().detalhes_conta(idconta)

    # Retornar contas pagas
    def obter_contas_recebidas(self):
        return self.get_queryset().contas_recebidas()

    # Retornar contas a pagar
    def obter_contas_nao_recebidas(self):
        return self.get_queryset().contas_nao_recebidas()

    # Retornar o total a receber no mes
    def obter_total_receber_mes(self, mes, ano):
        return self.get_queryset().total_receber_mes(mes, ano)

    # Obter soma das contas a receber por classificação
    def obter_soma_receber_classificacoes(self):
        return self.get_queryset().soma_receber_mes_classificacao()

    # Retornar contas com vencimento entre datas
    def obter_contas_expectativa_entre(self):
        return self.get_queryset().contas_entre_datas()


# Modelo das contas a receber
class ContasReceber(models.Model):

    class Meta:
        ordering = ('data_expectativa', 'valor')

    sit_escolha = [('R', 'Recebido'), ('N', 'Não recebido')]

    data_expectativa = models.DateField(auto_now=False, auto_now_add=False)

    data_recebimento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.DecimalField(
        null=False, default=0.00, max_digits=10, decimal_places=2)

    descricao = models.TextField(max_length=300, null=True)

    classificacao = models.ForeignKey(ClassificacaoReceber,
                                      on_delete=SET_NULL,
                                      null=True,
                                      default='SA')

    formapagar = models.ForeignKey(FormaPagamento,
                                   on_delete=SET_NULL,
                                   null=True)

    situacao = models.CharField(choices=sit_escolha,
                                default='N',
                                max_length=1)

    receber_objects = ReceberManager()

    def __str__(self):
        # Retorna descrição, situação, data de expectativa e valor
        return (f"{self.descricao} - {self.situacao} - {self.data_expectativa} - {self.valor}")
