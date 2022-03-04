from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.SlugField('Название тега', primary_key=True, allow_unicode=True)
    search_fields = ['name']

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



class Operation(models.Model):
    title = models.CharField('Название транзакции', max_length=100, blank=False, default='')
    transaction = models.DecimalField('операция', blank=False, max_digits=20, decimal_places=2)
    pub_date = models.DateTimeField('Дата транзакции', default=timezone.now)
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        blank=True,
        verbose_name='Теги',
    )
    
    
    def __str__(self):
        return f'{self.title}'
    
        
    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

