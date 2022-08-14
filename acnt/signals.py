from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from acnt.models import *

User = get_user_model()


@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    """
    Assign User roll and associate new profile for the user
    """
    if created:
        customer_type = instance.customer_type
        if customer_type == 'C':
            group = Group.objects.get(name=customer_type)
            customer_profile = CustomerProfile.objects.create(user=instance)
            customer_wallet = Wallet.objects.create(user=instance)
            group.user_set.add(instance)
        elif customer_type == 'V':
            group = Group.objects.get(name=customer_type)
            vendor_profile = VendorProfile.objects.create(user=instance)
            vendor_wallet = Wallet.objects.create(user=instance)
            group.user_set.add(instance)
        elif customer_type == 'C':
            group = Group.objects.get(name=customer_type)
            group.user_set.add(instance)
        # instance.groups.add(group)
        instance.save()
