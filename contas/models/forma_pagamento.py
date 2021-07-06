# -*- coding: utf-8 -*-
from django.db import models


# Classificação Pagar Manager
class FormasPagamentoManager(models.Manager):

    # Retonar todas as classificações de contas a pagar
    def obter_formas_pagamento(self):
        return self.all()

# Alterar para tabela com chave
class FormaPagamento(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='DI')
    descricao = models.CharField(max_length=20, null=False, default='Dinheiro')

    pagamentos_objects = FormasPagamentoManager()

    def __str__(self):
        return self.descricao
