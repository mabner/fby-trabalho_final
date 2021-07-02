# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.db.models.deletion import SET_NULL


class SituacaoPagar(models.Model):

    sit_escolha = [('P', 'Pago'), ('N', 'A pagar')]

    escolha = models.CharField(choices=sit_escolha,
                               default='N',
                               max_length=1)


# Alterar para tabela com chave
class FormaPagamento(models.Model):

    forma_escolha = [
        ('DI', 'Dinheiro'),
        ('BB', 'Boleto'),
        ('CC', 'Crédito'),
        ('CD', 'Débito'),
        ('DB', 'Depósito'),
        ('TR', 'Tranferência')
    ]

    forma_pagamento = models.CharField(
        choices=forma_escolha,
        default='DI',
        max_length=2)


# Alterar para tabela com chave
class ClassificacaoPagar(models.Model):

    class_escolha = [
        ('AG', 'Água'),
        ('LU', 'Luz'),
        ('TE', 'Telefone'),
        ('IN', 'Internet'),
        ('AL', 'Alimentação'),
        ('HO', 'Hobby'),
        ('OT', 'Outros'),
    ]

    classificacao_pagar = models.CharField(
        choices=class_escolha,
        default='OT',
        max_length=2)


class ContasPagar(models.Model):
    data_vencimento = models.DateField(null=False)
    data_pagamento = models.DateField(default=datetime.now(),
                                      null=False)
    valor = models.FloatField(null=False)
    descricao = models.TextField(max_length=300, null=True)
    classificacao = models.ForeignKey(ClassificacaoPagar,
                                      on_delete=SET_NULL,
                                      null=True)
    formapagar = models.ForeignKey(FormaPagamento,
                                   on_delete=SET_NULL,
                                   null=True)
    situacao = models.ForeignKey(SituacaoPagar,
                                 on_delete=SET_NULL,
                                 null=True)
