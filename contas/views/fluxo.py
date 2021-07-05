from django.shortcuts import render
from contas.models import *

# View


def fluxo_caixa(request):
  return render(request, 'fluxo.html')
