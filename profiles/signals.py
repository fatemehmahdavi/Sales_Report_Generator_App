from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(signal=post_save,sender=User)
#instance is an object that belongs to a class
def post_save_create_profile(sender,instance,created,**kwargs):
    #once the instance of the sender class(User) is created the profile of this instance(user) is created as well
    #created returns true only once one we create an instance of the sender class
    # print(instance)
    # print(created)
    if created:
        Profile.objects.create(user=instance)
