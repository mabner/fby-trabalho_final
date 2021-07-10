from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('formaspagamento', views.formas_pagamento, name='formaspagamento'),
    path('formaspagamento/cadastrar',
         views.cadastrar_formas_pagamento, name='cadastrar_pagamento'),
    path('classreceber', views.classificacao_receber, name='classreceber'),
    path('classpagar', views.classificacao_pagar, name='classpagar'),
    path('pagar', views.pagar, name='pagar'),
    path('receber', views.receber, name='receber'),
    path('receber/<int:idconta>',
         views.detalhar_conta_receber, name='detalhes_receber'),
    path('pagar/<int:idconta>',
         views.detalhar_conta_pagar, name='detalhes_pagar'),
    path('fluxo', views.fluxo_caixa, name='fluxo'),
    path('pagar/cadastrar', views.cadastrar_conta_pagar, name='cadastrar_pagar'),
    path('receber/cadastrar', views.cadastrar_conta_receber,
         name='cadastrar_receber'),
]
