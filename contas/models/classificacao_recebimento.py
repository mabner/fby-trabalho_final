# -*- coding: utf-8 -*-
from django.db import models


class ClassifReceberQuerySet(models.QuerySet):

    # Query para retornar a classificação do recebimento por ID
    def detalhes_classif_recebimento(self, id):
        return self.filter(id=id)


# Classifica Receber Manager
class ClassifReceberManager(models.Manager):

    def get_queryset(self):
        return ClassifReceberQuerySet(self.model, using=self._db)

    # Retonar todas as classificações de contas a receber
    def obter_classif_contas_receber(self):
        return self.all()

    # Retornar detalhes da classificação do ID informado
    def obter_detalhe_classif_recebimento(self, id):
        return self.get_queryset().detalhes_classif_recebimento(id)


# Modelo das classificações das contas a receber
class ClassificacaoReceber(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='SA')
    descricao = models.CharField(max_length=20, null=False, default='Salário')

    classif_receber_objects = ClassifReceberManager()

    def __str__(self):
        return self.descricao
