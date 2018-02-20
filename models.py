from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    QC = 1
    ON = 2
    BC = 3
    MB = 4
    AL = 5
    SK = 6
    NS = 7
    NB = 8
    ALL = 10
    PROVINCE_CHOICES = (
                           (QC, 'Quebec'),
                           (ON, 'Ontario'),
                           (BC, 'British-Columbia'),
                           (MB, 'Manitoba'),
                           (AL, 'Alberta'),
                           (SK, 'Saskatchewan'),
                           (NS, 'Nova-Scotia'),
                           (NB, 'New Brunswick'),
                           (ALL, 'All provinces'),
                        )
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    province = models.PositiveSmallIntegerField(choices=PROVINCE_CHOICES, verbose_name="Province", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    instance.profile.save()
