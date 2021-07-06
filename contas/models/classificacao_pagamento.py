# -*- coding: utf-8 -*-
from django.db import models

# Classificação Pagar Manager


class ClassifPagarManager(models.Manager):

    # Retonar todas as classificações de contas a pagar
    def obter_classif_contas_pagar(self):
        return self.all()

# Modelo da classificação de contas a pagar
class ClassificacaoPagar(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='OT')
    descricao = models.CharField(max_length=20, null=False, default='Outros')

    classif_pagar_objects = ClassifPagarManager()

    def __str__(self):
        return (f"{self.sigla} - {self.descricao}")
