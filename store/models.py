from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True, blank=True)
    image=models.ImageField(upload_to="images",null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total
    
    def __str__(self):
        return self.product.name
    
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    zipcode=models.CharField(max_length=6,null=False)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __Str__(self):
        return self.address
    