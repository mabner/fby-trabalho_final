# Generated by Django 3.2.3 on 2021-07-04 02:51

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
			('contas', '0005_auto_20210703_0146'),
			]

	operations = [
			migrations.AlterModelManagers(
					name='contaspagar',
					managers=[
							('pagar_objects', django.db.models.manager.Manager()),
							],
					),
			migrations.AlterModelManagers(
					name='contasreceber',
					managers=[
							('receber_objects', django.db.models.manager.Manager()),
							],
					),
			]
