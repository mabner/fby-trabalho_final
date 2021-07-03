# -*- coding: utf-8 -*-
from django import utils
from django.db import models
from django.db.models.deletion import SET_NULL
from .forma_pagamento import *


class SituacaoReceber(models.Model):

    sit_escolha = [('R', 'Recebido'), ('N', 'Não recebido')]

    escolha = models.CharField(choices=sit_escolha,
                               default='N',
                               max_length=1)

    def __str__(self):
        return self.escolha


class ClassificacaoReceber(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='SA')
    descricao = models.CharField(max_length=20, null=False, default='Salário')

    def __str__(self):
        return self.descricao


class ContasReceber(models.Model):
    data_expectativa = models.DateField(null=False)
    data_recebimento = models.DateField(default=utils.timezone.now, null=False)
    valor = models.FloatField(null=False, default=0)
    descricao = models.TextField(max_length=300, null=True)
    classificacao = models.ForeignKey(ClassificacaoReceber,
                                      on_delete=SET_NULL,
                                      null=True)
    formapagar = models.ForeignKey(FormaPagamento,
                                   on_delete=SET_NULL,
                                   null=True)
    situacao = models.ForeignKey(SituacaoReceber,
                                 on_delete=SET_NULL,
                                 null=True)
