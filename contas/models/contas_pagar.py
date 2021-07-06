# -*- coding: utf-8 -*-
from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.forma_pagamento import FormaPagamento
from django.db import models
from django.db.models import Sum
from django.db.models.deletion import SET_NULL


# Contas a Pagar QuerySet
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

    # Query para retornar o valor total das contas no mês
    def total_pagar_mes(self, mes, ano):
        return float(ContasPagar.pagar_objects.filter(data_vencimento__month=mes,
                                                      data_vencimento__year=ano)
                     .aggregate(Sum('valor'))['valor__sum'])

    # Query para retonar a soma do mês por classificação
    def soma_pagar_mes_classificacao(self, mes, ano):
        classificacoes = ClassificacaoPagar.objects.all().count()
        valores = []

        for class_id in range(1, classificacoes):
            soma_mes_class = float(ContasPagar.pagar_objects.filter(data_vencimento__month=mes,
                                                                    data_vencimento__year=ano,
                                                                    classificacao=class_id)
                                   .aggregate(Sum('valor'))['valor__sum'])

        valor = {'classificacao': ClassificacaoPagar.objects.get(id=class_id),
                 'soma_mes_class': soma_mes_class}
        if soma_mes_class > 0:
            valores.append(valor)

        return valores

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(vencimento__range=(dataInicio, dataFim))


# Contas a Pagar Manager
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

    # Retornar o total a pagar do mes
    def obter_total_pagar_mes(self, mes, ano):
        return self.get_queryset().total_pagar_mes(mes, ano)

    # Obter soma das contas a pagar por classificação
    def obter_soma_pagar_classificacoes(self, mes, ano):
        return self.get_queryset().soma_pagar_mes_classificacao(mes, ano)

    # Retornar contas com vencimento entre datas
    def obter_contas_vencimento_entre(self):
        return self.get_queryset().contas_entre_datas()


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
