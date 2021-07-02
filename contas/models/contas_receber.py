# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.deletion import SET_NULL
from .contas_pagar import FormaPagamento


class SituacaoReceber(models.Model):

    sit_escolha = [('R', 'Recebido'), ('N', 'Não recebido')]

    escolha = models.CharField(choices=sit_escolha,
                               default='N',
                               max_length=1)


# Alterar para tabela com chave
class ClassificacaoReceber(models.Model):
    class_escolha = [
        ('SE', 'Serviço prestado'),
        ('SA', 'Salário'),
        ('VE', 'Vendas'),
    ]

    classificacao_receber = models.CharField(
        choices=class_escolha,
        default='SE',
        max_length=2)


class ContasReceber(models.Model):
    data_expectativa = models.DateField(null=False)
    data_recebimento = models.DateField(null=False)
    valor = models.FloatField(null=False)
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
