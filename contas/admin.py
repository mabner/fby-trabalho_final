from django.contrib import admin
from .models import *

# Modelos pagar
admin.site.register(ContasPagar)
admin.site.register(ClassificacaoPagar)

# Modelos receber
admin.site.register(ContasReceber)
admin.site.register(ClassificacaoReceber)

# Modelo forma de pagamento
admin.site.register(FormaPagamento)
