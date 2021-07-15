# -*- coding: utf-8 -*-
from django.db import models


# Formas de pagamento QuerySet


class FormaPagamentoQuerySet(models.QuerySet):

	# Query para retornar forma de pagemento por ID
	def detalhes_forma_pagamento(self, id):
		return self.filter(id=id)


# Classificação Pagar Manager
class FormasPagamentoManager(models.Manager):

	def get_queryset(self):
		return FormaPagamentoQuerySet(self.model, using=self._db)

	# Retonar todas as classificações de contas a pagar
	def obter_formas_pagamento(self):
		return self.all()

	# Retornar detalhes da forma de pagamento do ID informado
	def obter_detalhe_forma_pagamento(self, id):
		return self.get_queryset().detalhes_forma_pagamento(id)


# Alterar para tabela com chave
class FormaPagamento(models.Model):
	sigla = models.CharField(max_length=2, null=False, default='DI')
	descricao = models.CharField(max_length=20, null=False, default='Dinheiro')

	pagamentos_objects = FormasPagamentoManager()

	def __str__(self):
		return self.descricao
