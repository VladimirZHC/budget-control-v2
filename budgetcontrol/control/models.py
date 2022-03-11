from django.db import models
# from simple_history.models import HistoricalRecords




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
    pub_date = models.DateTimeField('Дата транзакции', auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField('Дата изменения транзакции', auto_now=True, null=True, blank=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        blank=True,
        verbose_name='Теги',
    )
    # history = HistoricalRecords(inherit=True)
    
   
    def __str__(self):
        return f'{self.title}'
    
        
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
        
        
        
class HistoryOperation(models.Model):
    operation = models.ForeignKey(Operation, related_name='history', on_delete=models.CASCADE)
    title = models.CharField('Название транзакции', max_length=100, blank=False, default='')
    transaction = models.DecimalField('операция', blank=False, max_digits=20, decimal_places=2)
    up_day = models.DateTimeField('Дата изменения транзакции', auto_now_add=True, null=True, blank=True)
    tags = models.CharField('Теги', max_length=30, blank=True, null=True)
    
    
    def __str__(self):
        return f' История транзакции: { self.operation}'
    
    
    class Meta:
        verbose_name = 'Историю'
        verbose_name_plural = 'Истории'