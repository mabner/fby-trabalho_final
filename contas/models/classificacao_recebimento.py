# -*- coding: utf-8 -*-
from django.db import models


# Classifica Receber Manager
class ClassifReceberManager(models.Manager):

    # Retonar todas as classificações de contas a receber
    def obter_classif_contas_receber(self):
        return self.all()

# Modelo das classificações das contas a receber
class ClassificacaoReceber(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='SA')
    descricao = models.CharField(max_length=20, null=False, default='Salário')

    classif_receber_objects = ClassifReceberManager()

    def __str__(self):
        return self.descricao
