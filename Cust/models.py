from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)
class Customers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

class Products(models.Model):
    categories=(
        ("M","Men"),
        ("W","women"),
        ("K","kids"),
        )
    title=models.CharField(max_length=50)
    selling_cost=models.FloatField()
    category=models.CharField(choices=categories,max_length=2)
    colour=models.CharField(max_length=50,default=None,null=True)
    discounted_price=models.FloatField()
    image=models.ImageField(upload_to="productimg")
   
   
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity *  self.product.discounted_price


class Orderhistory(models.Model):
    STATAUS_CHOICES=(
        ("Accepted","accepted"),
        ("Packed","packed"),
        ("On The Way","on the way"),
        ("Deleivered","delivered"),
        ("Cancel","canceled")
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATAUS_CHOICES,max_length=50,default="pending")

    @property
    def total_cost(self):
        return self.quantity *  self.product.discounted_price


    def __str__(self):
        return str(self.id)