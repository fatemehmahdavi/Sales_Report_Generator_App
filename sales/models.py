from email.policy import default
import profile
from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
# Create your models here.
#position=product*quanitity
class Position(models.Model):
    #whenever a product gets deleted all the positions to this product get deleted as well
    product=models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity=models.PositiveBigIntegerField()
    #by setting blank True,I want the price to be updated automatically by overriding the save method
    price=models.FloatField(blank=True) #blank=True means this field is optional
    created=models.DateTimeField(blank=True)
#Think your super() is a gateway to the inherited class, you can call the methods of the parent class via super().
# When you say that you want to override something in the parent method you necessarily only want to add to what the existing method is providing.
    def save(self,*args,**kwargs):
        self.price=self.product.price*self.quantity
#we do not know what arguments save is expecting so this is basically saying "any arguments passed into our new save(…) method, 
# just hand them off to the old overridden save(…) method, positional arguments first followed by any keyword arguments"   
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"id:{self.id},product:{self.product.name},quantity:{self.quantity}"
#each sale object can have many positions
class Sale(models.Model):
    #transaction_id will be generated automatically so to do this I set the blank=True and override the save method
    transaction_id=models.CharField(max_length=12,blank=True)
    positions=models.ManyToManyField(Position) #the list of positions that we are including in the sale object
    total_price=models.FloatField(blank=True,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    salesman=models.ForeignKey(Profile,on_delete=models.CASCADE)
    created=models.DateTimeField(blank=True)
    updated=models.DateTimeField(auto_now=True) #Any field with the auto_now attribute set will also inherit editable=False and will not show up in the admin panel. 

    def __str__(self):
        return f"sales for the amount of ${self.total_price}"
    
    def save(self,*args, **kwargs):
        if self.transaction_id=="":
            self.transaction_id=generate_code()
        if self.created==None:
            self.created=timezone.now()
        return super().save(*args, **kwargs)
    def get_positions(self):
        return self.positions.all()

class CSV(models.Model):
    file_name=models.FileField(upload_to='csv')
    activated=models.BooleanField(default=False) #if we've used a file already or not
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file_name