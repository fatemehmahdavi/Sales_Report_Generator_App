from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
#each class is like a table in the database
#The class includes fields which are the columns in the database
#each object of the class is like a row in the table
#each class inherits from Model class
#models is a library
class Customer(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='customers',default='no_picture.png')
    # read this page about __str__()https://www.digitalocean.com/community/tutorials/python-str-repr-functions
# each cumstomer coming out of the Customer class wil be represeneted with the string representation which is referring to the name
    def __str__(self):
        return str(self.name)
# c=Customer('negar')
# print(c)
# print(c.__repr__())
# print(c.__str__())
        