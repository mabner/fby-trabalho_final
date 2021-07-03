# -*- coding: utf-8 -*-
from django.db import models


# Alterar para tabela com chave
class FormaPagamento(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='DI')
    descricao = models.CharField(max_length=20, null=False, default='Dinheiro')

    def __str__(self):
        return self.descricao
