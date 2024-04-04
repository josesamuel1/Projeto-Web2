# Generated by Django 5.0.3 on 2024-04-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEstoque', '0003_alter_produto_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(choices=[('G', 'g'), ('P', 'p'), ('PP', 'pp'), ('GG', 'gg'), ('M', 'm'), ('XG', 'xg')], default='', max_length=2),
        ),
    ]
