
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Itemlist

@receiver(pre_save, sender=Itemlist)
def print_itemlist_pre_save(sender, instance, **kwargs):
    print(f"Object state before save (pre_save) for {sender.__name__} with id {instance.id}:")
    print(f"Current attributes:")
    print(f"Name: {instance.name}")
    print(f"Price: {instance.price}")
    print(f"Discount: {instance.discount}")
    print("")

@receiver(post_save, sender=Itemlist)
def print_itemlist_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Object state after save (post_save) for newly created {sender.__name__} with id {instance.id}:")
    else:
        print(f"Object state after save (post_save) for {sender.__name__} with id {instance.id}:")
    print(f"Current attributes:")
    print(f"Name: {instance.name}")
    print(f"Price: {instance.price}")
    print(f"Discount: {instance.discount}")
    print("")
