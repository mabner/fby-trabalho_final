# Generated by Django 3.2.3 on 2021-07-04 02:52

from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
			('contas', '0007_auto_20210703_2351'),
			]

	operations = [

			migrations.RunSQL(
					sql=[
							# Contas a pagar
							(
									"INSERT INTO contas_contaspagar (data_vencimento, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-06-11', 180, 'Yellow Coris', 'P', 6, 6)"),
							(
									"INSERT INTO contas_contaspagar (data_vencimento, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-06-12', 96, 'Verdurao', 'P', 5, 4)"),
							(
									"INSERT INTO contas_contaspagar (data_vencimento, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-07-20', 230, 'Supermercado', 'N', 5, 4)"),
							(
									"INSERT INTO contas_contaspagar (data_vencimento, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-07-01', 129, 'Racoes novas', 'P', 6, 3)"),
							# Contas a receber
							(
									"INSERT INTO contas_contasreceber (data_expectativa, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-07-05', 110, 'Vale alimentacao', 'N', 2, 5)"),
							(
									"INSERT INTO contas_contasreceber (data_expectativa, valor, descricao, situacao, classificacao_id, formapagar_id) VALUES ('2021-07-05', 1700, 'Salario', 'N', 2, 5)"),
							],
					),
			]
