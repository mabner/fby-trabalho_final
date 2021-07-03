# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.deletion import SET_NULL
from .forma_pagamento import *


# Contas QuerySet
class ReceberQuerySet(models.QuerySet):
    # Query para retornar as contas recebidas
    def contas_recebidas(self):
        return self.filter(situacao="R")

    # Query para retonar as contas não recebidas
    def contas_nao_recebidas(self):
        return self.filter(situacao="N")

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(data_expectativa__range=(dataInicio, dataFim))


# Contas Manager
class ReceberManager(models.Manager):

    def get_queryset(self):
        return ReceberQuerySet(self.model, using=self._db)

    # Retornar todas as contas
    def obter_todas_contas_receber(self):
        return self.all()

    # Retornar contas pagas
    def obter_contas_recebidas(self):
        return self.get_queryset().contas_recebidas()

    # Retornar contas a pagar
    def obter_contas_nao_recebidas(self):
        return self.get_queryset().contas_nao_recebidas()

    # Retornar contas com vencimento entre datas
    def obter_contas_expectativa_entre(self):
        return self.get_queryset().contas_entre_datas()


# Modelo das classificações das contas a receber
class ClassificacaoReceber(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='SA')
    descricao = models.CharField(max_length=20, null=False, default='Salário')

    def __str__(self):
        return self.descricao

# Modelo das contas a receber


class ContasReceber(models.Model):

    sit_escolha = [('R', 'Recebido'), ('N', 'Não recebido')]

    data_expectativa = models.DateField(auto_now=False, auto_now_add=False)

    data_recebimento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.FloatField(null=False, default=0)

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
