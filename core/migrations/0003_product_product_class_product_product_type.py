# Generated by Django 5.1.1 on 2024-10-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_class',
            field=models.CharField(choices=[('Bond', 'Bond'), ('Equity', 'Equity'), ('Interst', 'Interest'), ('Forex', 'Forex'), ('Commodities', 'Commodities')], default='Bond', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('Option', 'Option'), ('Forward', 'Forward'), ('Future', 'Future'), ('Swap', 'Swap'), ('SwapCrossCurrency', 'SwapCrossCurrency'), ('Spot', 'Spot'), ('Standard', 'Standard')], default='Standard', max_length=20),
        ),
    ]
