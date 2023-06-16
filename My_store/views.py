from django.shortcuts import render,redirect
from Cust.models import *
from django.views import View
from django.db.models import Q
from django.contrib.auth.decorators import login_required


class Home(View):
    def get(self,request):
        men=Products.objects.filter(category="M")
        women=Products.objects.filter(category="W")
        kids=Products.objects.filter(category="K")
        return render(request,"index.html",{"men":men,"women":women,"kids":kids})

class Products_total(View):
    def get(self,request):
        products= Products.objects.all()
        return render(request,"products.html",{"products":products})

class Single_product(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        if request.user.is_authenticated:
            prod_already_in_cart=False
            prod_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists() 
            return render(request,"single-product.html",{"product":product,"prod_already_in_cart":prod_already_in_cart})
        else:
            return render(request,"single-product.html",{"product":product})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

@login_required
def checkout(request):
    carts=Cart.objects.filter(user=request.user)
    if carts:
        custs=Customers.objects.filter(user=request.user)
        overall_cost=0
        shippingcost=70
        for cart in carts:
            temp_cost = cart.quantity * cart.product.discounted_price
            overall_cost += temp_cost
        total_amount=overall_cost + shippingcost
        return render(request,"cart/checkout.html",{"custs":custs,"carts":carts,"overall_cost":overall_cost,"total_amount":total_amount})
    else:
        return render(request,"cart/emptycart.html",{"cart":carts})

@login_required
def payment_done(request): 
    custid=request.GET.get("custid")
    customer=Customers.objects.get(id=custid)
    carts=Cart.objects.filter(user=request.user)
    for cart in carts:
        Orderhistory(user=request.user,customer=customer,product=cart.product
                    ,quantity=cart.quantity).save()
        cart.delete()
    return redirect("/orderhist")

@login_required
def orderhistory(request):
    hist=Orderhistory.objects.filter(user=request.user)
    return render(request,"cust/orderhistory.html",{"orderhists":hist,"active":"btn-dark"})   
    