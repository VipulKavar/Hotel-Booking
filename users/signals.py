from Tools.demo.mcast import sender
from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    instance.profile.save()
