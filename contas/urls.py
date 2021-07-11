from django.urls import path

from . import views

urlpatterns = [
		# Root
		path('', views.index, name='index'),

		# Formas de Pagamento
		path('formaspagamento', views.formas_pagamento, name='formaspagamento'),
		path('formaspagamento/cadastrar',
		     views.cadastrar_formas_pagamento, name='cadastrar_pagamento'),
		path('formaspagamento/<int:id>',
		     views.detalhar_forma_pagamento, name='detalhes_forma_pagamento'),
		path('formaspagamento/apagar/<int:id>',
		     views.apagar_forma_pagamento, name='apagar_forma_pagamento'),

		# Classificações das contas
		path('classreceber', views.classificacao_receber, name='classreceber'),
		path('classpagar', views.classificacao_pagar, name='classpagar'),

		# Contas a pagar
		path('pagar', views.pagar, name='pagar'),
		path('pagar/<int:idconta>',
		     views.detalhar_conta_pagar, name='detalhes_pagar'),
		path('pagar/cadastrar', views.cadastrar_conta_pagar, name='cadastrar_pagar'),

		# Contas a receber
		path('receber', views.receber, name='receber'),
		path('receber/<int:idconta>',
		     views.detalhar_conta_receber, name='detalhes_receber'),
		path('receber/cadastrar', views.cadastrar_conta_receber,
		     name='cadastrar_receber'),

		# Fluxo de caixa
		path('fluxo', views.fluxo_caixa, name='fluxo'),
		path('fluxoprevisto', views.fluxo_previsto, name='fluxo_previsto'),
		path('fluxorealizado', views.fluxo_realizado, name='fluxo_realizado'),

		]
