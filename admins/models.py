from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Admins(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_h20u41'

)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_Admin(sender, instance, created, **kwargs):
    if created:
        Admin.objects.create(owner=instance)


post_save.connect(create_Admin, sender=User)