# -*- coding: utf-8 -*-
from contas.managers import PagarManager
from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.forma_pagamento import FormaPagamento
from django.db import models
from django.db.models.deletion import SET_NULL


# Modelo das contas a pagar
class ContasPagar(models.Model):

    class Meta:
        ordering = ('data_vencimento', 'valor')

    sit_escolha = [('S', 'Pago'), ('N', 'A pagar')]

    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)

    data_pagamento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.DecimalField(
        null=False, default=0.00, max_digits=10, decimal_places=2)

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

    pagar_objects = PagarManager()

    def __str__(self):
        # Retorna descrição, situação, data vencimento e valor
        return (f"{self.descricao} - {self.situacao} - {self.data_vencimento} - {self.valor}")
