# Generated by Django 5.1 on 2024-10-03 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bankaccount')),
            ],
        ),
    ]
