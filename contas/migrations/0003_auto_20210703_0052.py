# Generated by Django 3.2.3 on 2021-07-03 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_auto_20210703_0051'),
    ]

    operations = [
        # Classificação contas a pagar
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['AG', 'Água'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['AG'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['LU', 'Luz'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['LU'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['TE', 'Telefone'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['TE'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['IN', 'Internet'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['IN'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['AL', 'Alimentação'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['AL'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['HO', 'Hobby'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['HO'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaopagar (sigla, descricao) VALUES (%s, %s);", ['OT', 'Outros'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaopagar where sigla=%s;", ['OT'])],
        ),
        # Formas de pagamento
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['DI', 'Dinheiro'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['DI'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['BB', 'Boleto'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['BB'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['CC', 'Crédito'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['CC'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['CD', 'Débito'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['CD'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['DP', 'Depósito'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['DP'])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_formapagamento (sigla, descricao) VALUES (%s, %s);", ['TR', 'Tranferência'])],
            reverse_sql=[
                ("DELETE FROM contas_formapagamento where sigla=%s;", ['TR'])],
        ),
        # Classificação contas a receber
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaoreceber (sigla, descricao) VALUES (%s, %s);", ['SE', 'Serviço prestado'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaoreceber where sigla=%s;", [''])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaoreceber (sigla, descricao) VALUES (%s, %s);", ['SA', 'Salário'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaoreceber where sigla=%s;", [''])],
        ),
        migrations.RunSQL(
            sql=[
                ("INSERT INTO contas_classificacaoreceber (sigla, descricao) VALUES (%s, %s);", ['VE', 'Vendas'])],
            reverse_sql=[
                ("DELETE FROM contas_classificacaoreceber where sigla=%s;", [''])],
        ),
    ]
