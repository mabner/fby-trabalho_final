# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.deletion import SET_NULL
from .forma_pagamento import *
from django.db.models import Sum


# Contas QuerySet
class PagarQuerySet(models.QuerySet):
    # Query para retornar as contas pagas
    def contas_pagas(self):
        return self.filter(situacao="P")

    # Query para retornar os detalhes da conta a pagar
    def detalhes_conta(self, idconta):
        return self.filter(id=idconta)

    # Query para retonar as contas em aberto
    def contas_em_aberto(self):
        return self.filter(situacao="N")

    # Query para retornar o valor total das contas em aberto
    def total_em_aberto(self):
        return float(self.filter(situacao="N").aggregate(
            Sum('valor'))['valor__sum'])

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(vencimento__range=(dataInicio, dataFim))


# Contas Manager
class PagarManager(models.Manager):

    def get_queryset(self):
        return PagarQuerySet(self.model, using=self._db)

    # Retornar todas as contas
    def obter_todas_contas_pagar(self):
        return self.all()

    # Retornar a soma das contas em aberto
    def obter_total_em_aberto(self):
        return self.get_queryset().total_em_aberto()

    # Retornar detalhes da conta
    def obter_detalhes_conta(self, idconta):
        return self.get_queryset().detalhes_conta(idconta)

    # Retornar contas pagas
    def obter_contas_pagas(self):
        return self.get_queryset().contas_pagas()

    # Retornar contas a pagar
    def obter_contas_em_aberto(self):
        return self.get_queryset().contas_em_aberto()

    # Retornar contas com vencimento entre datas
    def obter_contas_vencimento_entre(self):
        return self.get_queryset().contas_entre_datas()


# Modelo da classificação de contas a pagar
class ClassificacaoPagar(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='OT')
    descricao = models.CharField(max_length=20, null=False, default='Outros')

    def __str__(self):
        return self.descricao


# Modelo das contas a pagar
class ContasPagar(models.Model):

    sit_escolha = [('S', 'Pago'), ('N', 'A pagar')]

    data_vencimento = models.DateField(auto_now=False, auto_now_add=False)

    data_pagamento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    valor = models.FloatField(null=False, default=0.00)

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
