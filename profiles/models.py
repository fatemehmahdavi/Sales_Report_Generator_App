from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    #each user can only have one profile
    #whenever the user gets deleted the profile of the user gets deleted as well
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    bio=models.TextField()
    avatar=models.ImageField(upload_to='avatars',blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"
