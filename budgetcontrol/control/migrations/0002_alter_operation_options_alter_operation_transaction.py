# Generated by Django 4.0.2 on 2022-02-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ('pub_date',), 'verbose_name': 'Операция', 'verbose_name_plural': 'Операции'},
        ),
        migrations.AlterField(
            model_name='operation',
            name='transaction',
            field=models.FloatField(default=0.0, verbose_name='операция'),
        ),
    ]
