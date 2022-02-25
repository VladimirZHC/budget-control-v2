from django.db import models
from django.utils import timezone
# from pygments.lexers import get_all_lexers

# from pygments.styles import get_all_styles
# LEXERS = [item for item in get_all_lexers() if item[1]]


class Operation(models.Model):
    title = models.CharField('Название транзакции', max_length=100, blank=False, default='')
    transaction = models.FloatField('операция', blank=False, default=0.0)
    pub_date = models.DateTimeField('Дата транзакции', default=timezone.now)
    
    
    def __str__(self):
        return f'{self.title}'
    
        
    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
