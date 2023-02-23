from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Customer, Driver, CustomerProfile, DriverProfile


@receiver(post_save, sender=Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(customer=instance)


@receiver(post_save, sender=Customer)
def save_customer_profile(sender, instance, **kwargs):
    instance.customerprofile.save()



@receiver(post_save, sender=Driver)
def create_driver_profile(sender, instance, created, **kwargs):
    if created:
        DriverProfile.objects.create(driver=instance)


@receiver(post_save, sender=Driver)
def save_driver_profile(sender, instance, **kwargs):
    instance.driverprofile.save()
