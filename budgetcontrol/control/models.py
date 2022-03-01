from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.db.models.functions import Coalesce
from django.db.models import Sum
# from pygments.lexers import get_all_lexers

# from pygments.styles import get_all_styles
# LEXERS = [item for item in get_all_lexers() if item[1]]


class Operation(models.Model):
    title = models.CharField('Название транзакции', max_length=100, blank=False, default='')
    transaction = models.DecimalField('операция', blank=False, max_digits=20, decimal_places=2)
    pub_date = models.DateTimeField('Дата транзакции', default=timezone.now)
    
    
    def __str__(self):
        return f'{self.title}'
    
    # вот тут подсчитывается итог и заносится в поле 'total'
    @property
    def total(self):
        return Decimal(
            Operation.objects
            .aggregate(total=Coalesce(Sum('transaction'), Decimal(0)))['total']
        )
    
        
    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

