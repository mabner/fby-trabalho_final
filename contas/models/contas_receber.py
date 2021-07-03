# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.deletion import SET_NULL
from .forma_pagamento import *


class ClassificacaoReceber(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='SA')
    descricao = models.CharField(max_length=20, null=False, default='Salário')

    def __str__(self):
        return self.descricao


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

    def __str__(self):
        return (f"{self.descricao} - {self.situacao} - {self.data_expectativa} - {self.valor}")
