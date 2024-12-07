# Generated by Django 5.1.3 on 2024-11-14 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('descricao', models.CharField(max_length=45, verbose_name='Descição')),
                ('cod_barras', models.CharField(max_length=45, verbose_name='Código')),
                ('quantidade', models.IntegerField(default=1)),
                ('tamanho', models.CharField(max_length=45, verbose_name='Tamanho')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
                ('cor_id', models.ManyToManyField(to='core.cor')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoCor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cor')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
        ),
    ]
