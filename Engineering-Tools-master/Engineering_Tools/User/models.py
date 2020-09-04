from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    address_line = models.TextField()
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 15)
    country = models.CharField(max_length = 15)
    pincode = models.CharField(max_length = 6)

    def __str__(self):
        return  self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance, email = instance.email)


