from .models import *
from django.db.models import QuerySet, Manager
from django.db.models import Sum


# Contas a Pagar QuerySet
class PagarQuerySet(QuerySet):
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
        soma_mes_class = float(ContasPagar.pagar_objects.filter(data_vencimento__month=mes,
                                                                data_vencimento__year=ano,
                                                                classificacao=classificacao)
                               .aggregate(Sum('valor'))['valor__sum'])

    pass

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(vencimento__range=(dataInicio, dataFim))


# Contas a Receber QuerySet
class ReceberQuerySet(QuerySet):
    # Query para retornar as contas recebidas
    def contas_recebidas(self):
        return self.filter(situacao="R")

    # Query para retornar os detalhes da conta a receber
    def detalhes_conta(self, idconta):
        return self.filter(id=idconta)

    # Query para retonar as contas não recebidas
    def contas_nao_recebidas(self):
        return self.filter(situacao="N")

    # Query para retornar o valor total das contas a receber
    def total_a_receber(self):
        return float(self.filter(situacao="N").aggregate(
            Sum('valor'))['valor__sum'])

    # Query para retornar o valor total das contas no mês
    def total_receber_mes(self, mes, ano):
        return float(ContasReceber.receber_objects.filter(data_expectativa__month=mes,
                                                          data_expectativa__year=ano)
                     .aggregate(Sum('valor'))['valor__sum'])

    # Query para retonar a soma do mês por classificação
    def soma_receber_mes_classificacao(self, mes, ano):
        soma_mes_class = float(ContasReceber.receber_objects.filter(data_expectativa__month=mes,
                                                                    data_expectativa__year=ano,
                                                                    classificacao=classificacao)
                               .aggregate(Sum('valor'))['valor__sum'])

    pass

    # Query para retornar contas entre período
    def contas_entre_datas(self, dataInicio, dataFim):
        return self.filter(data_expectativa__range=(dataInicio, dataFim))


# Contas a Pagar Manager
class PagarManager(Manager):

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


# Contas a Receber Manager
class ReceberManager(Manager):

    def get_queryset(self):
        return ReceberQuerySet(self.model, using=self._db)

    # Retornar todas as contas
    def obter_todas_contas_receber(self):
        return self.all()

    # Retornar a soma das contas em aberto
    def obter_total_a_receber(self):
        return self.get_queryset().total_a_receber()

    # Retornar detalhes da conta
    def obter_detalhes_conta(self, idconta):
        return self.get_queryset().detalhes_conta(idconta)

    # Retornar contas pagas
    def obter_contas_recebidas(self):
        return self.get_queryset().contas_recebidas()

    # Retornar contas a pagar
    def obter_contas_nao_recebidas(self):
        return self.get_queryset().contas_nao_recebidas()

    # Retornar contas com vencimento entre datas
    def obter_contas_expectativa_entre(self):
        return self.get_queryset().contas_entre_datas()


# Classifica Receber Manager
class ClassifReceberManager(Manager):

    # Retonar todas as classificações de contas a receber
    def obter_classif_contas_receber(self):
        return self.all()


# Classificação Pagar Manager
class ClassifPagarManager(Manager):

    # Retonar todas as classificações de contas a pagar
    def obter_classif_contas_pagar(self):
        return self.all()
