from .models import Operation, HistoryOperation
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=Operation)
def create_history(sender, instance, created, **kwargs):
    HistoryOperation.objects.create(
        operation = instance,
        title = instance.title,
        transaction=instance.transaction,
        tags = list(instance.tags.values_list(flat=True))          
        )