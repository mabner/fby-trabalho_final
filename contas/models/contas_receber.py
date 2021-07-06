# -*- coding: utf-8 -*-
from contas.managers import ReceberManager
from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.forma_pagamento import FormaPagamento
from django.db import models
from django.db.models.deletion import SET_NULL


# Modelo das contas a receber
class ContasReceber(models.Model):

    sit_escolha = [('R', 'Recebido'), ('N', 'Não recebido')]

    data_expectativa = models.DateField(auto_now=False, auto_now_add=False)

    data_recebimento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.FloatField(null=False, default=0.00)

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
