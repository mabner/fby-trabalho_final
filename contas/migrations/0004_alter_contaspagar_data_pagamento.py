# Generated by Django 3.2.3 on 2021-07-03 04:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
			('contas', '0003_auto_20210703_0132'),
			]

	operations = [
			migrations.AlterField(
					model_name='contaspagar',
					name='data_pagamento',
					field=models.DateField(default=django.utils.timezone.now),
					),
			]
