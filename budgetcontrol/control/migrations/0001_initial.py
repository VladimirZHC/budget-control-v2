# Generated by Django 4.0.2 on 2022-03-11 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.SlugField(allow_unicode=True, primary_key=True, serialize=False, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название транзакции')),
                ('transaction', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='операция')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата транзакции')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения транзакции')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='control.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='HistoryOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название транзакции')),
                ('transaction', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='операция')),
                ('up_day', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата изменения транзакции')),
                ('tags', models.CharField(blank=True, max_length=30, null=True, verbose_name='Теги')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='control.operation')),
            ],
            options={
                'verbose_name': 'Историю',
                'verbose_name_plural': 'Истории',
            },
        ),
    ]
