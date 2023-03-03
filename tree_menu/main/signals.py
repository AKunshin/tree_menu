from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import MenuItem

@receiver(pre_save, sender=MenuItem)
def set_nesting_level(sender, instance, **kwargs):
    if instance.parrent:
        instance.nesting_level = instance.parrent.nesting_level + 1
    else:
        instance.nesting_level = 1