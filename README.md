# Estrutura

## Contas a pagar
### Contas a pagar
  - data vencimento
  - data pagamento
  - valor
  - descrição conta
  - classificação conta
  - forma de pagamento
  - situação

### Classificação
  - telefone
  - água
  - energia
  - alimentação

### Forma de Pagamento
  - boleto
  - crédito
  - débito
  - depósito
  - transferência

### Situação
  - pago
  - a pagar
___


## Contas a receber

### Contas a receber
  - data de expectativa
  - data de recebimento
  - valor
  - descrição
  - classificação
  - forma de recebimento
  - situação

### Classificação
  - serviço prestado
  - salário
  - vendas

### Forma de recebimento
  - boleto
  - crédito
  - débito
  - depósito
  - transferência

### Situação
  - recebido
  - a receber
___


## Relatórios

- contas a pagar por período (data de vencimento)
- contas a receber por período (data expectativa)

___


## Telas

- fluxo de caixa (exibir mês a mês de no mínimo 6 meses)
- fluxo previsto (a receber e a pagar)
- fluxo realizado (recebido e pago)

O fluxo deverá exibir:
- saldo inicial,
- as receitas por classificação
- um totalizador de receitas
- despesas por classificação
- totalizador de despesas

No final da tabela, apresentar o saldo final e a lucratividade no período (diferença entre o saldo final e inicial)
- saldo inicial de um mês é o saldo final do mês anterior
- possível informar o valor para o primeiro mês manualmente

### Critérios de avaliação (total de 60pts):
- Adequação da camada de modelo: 8pts
- Adequação das rotas/views: 8pts
- Adequação dos templates: 8pts
- Implementação contas a pagar: 8pts
- Implementação contas a receber: 8pts
- Implementação relatórios de listagem: 6pts
- Implementação fluxo de caixa: 14pts