from django.contrib import admin
from .models import *

# Modelos pagar
admin.site.register(ContasPagar)
admin.site.register(ClassificacaoPagar)
admin.site.register(SituacaoPagar)

# Modelos receber
admin.site.register(ContasReceber)
admin.site.register(ClassificacaoReceber)
admin.site.register(SituacaoReceber)

# Modelo forma de pagamento
admin.site.register(FormaPagamento)
