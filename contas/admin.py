from contas.models.forma_pagamento import FormaPagamento
from contas.models.classificacao_recebimento import ClassificacaoReceber
from contas.models.contas_receber import ContasReceber
from contas.models.classificacao_pagamento import ClassificacaoPagar
from contas.models.contas_pagar import ContasPagar
from django.contrib import admin


# Modelos pagar
admin.site.register(ContasPagar)
admin.site.register(ClassificacaoPagar)

# Modelos receber
admin.site.register(ContasReceber)
admin.site.register(ClassificacaoReceber)

# Modelo forma de pagamento
admin.site.register(FormaPagamento)
