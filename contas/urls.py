from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('formaspagamento', views.formas_pagamento, name='formaspagamento'),
    path('classreceber', views.classif_receber, name='classreceber'),
    path('classpagar', views.classif_pagar, name='classpagar'),
    path('pagar', views.pagar, name='pagar'),
    path('receber', views.receber, name='receber'),
    path('receber/<int:idconta>',
         views.detalhar_conta_receber, name='detalhes_receber'),
    path('pagar/<int:idconta>',
         views.detalhar_conta_pagar, name='detalhes_pagar')
]
