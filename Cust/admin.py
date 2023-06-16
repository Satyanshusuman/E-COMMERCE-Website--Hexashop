from django.contrib import admin
from.models import *

# Register your models here.
@admin.register(Customers)
class Customeradmin(admin.ModelAdmin):
    list_display=["id","user","name","locality","city","zipcode","state"]

@admin.register(Products)
class Productadmin(admin.ModelAdmin):
    list_display=["id","title","colour","selling_cost","category","discounted_price","image"]

@admin.register(Cart)
class Cartadmin(admin.ModelAdmin):
    list_display=["id","user","product","quantity"]

@admin.register(Orderhistory)
class Historyadmin(admin.ModelAdmin):
    list_display=["id","user","customer","product","quantity","ordered_date","status"]
