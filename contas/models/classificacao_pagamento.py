# -*- coding: utf-8 -*-
from contas.managers import ClassifPagarManager
from django.db import models


# Modelo da classificação de contas a pagar
class ClassificacaoPagar(models.Model):

    sigla = models.CharField(max_length=2, null=False, default='OT')
    descricao = models.CharField(max_length=20, null=False, default='Outros')

    classif_pagar_objects = ClassifPagarManager()

    def __str__(self):
        return (f"{self.sigla} - {self.descricao}")
