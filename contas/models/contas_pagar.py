# -*- coding: utf-8 -*-
from django import utils
from django.db import models
from django.db.models.deletion import SET_NULL
from .forma_pagamento import *


class ClassificacaoPagar(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='OT')
    descricao = models.CharField(max_length=20, null=False, default='Outros')

    def __str__(self):
        return self.descricao


class ContasPagar(models.Model):

    sit_escolha = [('S', 'Pago'), ('N', 'A pagar')]

    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)

    data_pagamento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.FloatField(null=False, default=0)

    descricao = models.TextField(max_length=300, null=True)

    classificacao = models.ForeignKey(ClassificacaoPagar,
                                      max_length=1,
                                      null=True,
                                      on_delete=SET_NULL)

    formapagar = models.ForeignKey(FormaPagamento,
                                   on_delete=SET_NULL,
                                   null=True)

    situacao = models.CharField(choices=sit_escolha,
                                default='N',
                                max_length=1)

    def __str__(self):
        return (f"{self.descricao} - {self.situacao} - {self.data_vencimento} - {self.valor}")
