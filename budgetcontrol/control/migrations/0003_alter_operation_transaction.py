# Generated by Django 4.0.2 on 2022-02-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_alter_operation_options_alter_operation_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='transaction',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='операция'),
        ),
    ]
