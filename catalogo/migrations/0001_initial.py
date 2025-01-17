# Generated by Django 5.0.7 on 2024-07-19 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modadalidade',
            fields=[
                ('index', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('index', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('relacao', models.CharField(choices=[('vl', 'velocidades'), ('un', 'unica')], max_length=250)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.modadalidade')),
            ],
        ),
    ]
