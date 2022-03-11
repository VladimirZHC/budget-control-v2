from .models import Operation, HistoryOperation
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Operation)
def create_history(sender, instance, created, **kwargs):
    if created:
        HistoryOperation.objects.create(
            operation = instance,
            title = instance.title,
            transaction=instance.transaction,
            tags = instance.tags.values_list()                      
            )

# @receiver(post_save, sender=Operation)
# def save_history(sender, instance, **kwargs):
#     instance.operation.save()