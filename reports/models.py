from django.db import models

from profiles.models import Profile

# Create your models here.
#the report can contain many sale objects
class Report(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='reports',blank=True)    #store the charts based on the (date from) to the (date to)
    remarks=models.TextField() #write our thoughts based on the generated charts, like the sale of tv has decreased
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name