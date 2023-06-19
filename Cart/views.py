from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from Cust.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def add_cart(request):
    if request.user.is_authenticated:
        usr=request.user
        id=request.POST.get("product_id")
        product=Products.objects.get(id=id)
        quantity=request.POST.get("quantity")
        Cart(user=usr,product=product,quantity=quantity).save()
        return redirect ("/showcart/")
    else:
        return redirect("/Cust/login/")
    
@method_decorator(login_required,name="dispatch")
class  showcart(View):
    def get(self,request):
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            overallcost=0
            shippingcost=70
            total_qty=0
            if cart:
                for obj in cart:
                    temp_cost= obj.quantity * obj.product.discounted_price
                    overallcost += temp_cost
                    total_qty += obj.quantity
                total_cost=overallcost + shippingcost 
                return render(request,"cart/cart.html",{"carts":cart,"amount":overallcost,"totalamount":total_cost,"total_qty":total_qty})
            else:
                return render(request,"cart/emptycart.html",{"cart":cart})  
        else:
            return redirect("/Cust/login/")
        
@login_required        
def plus_cart(request):
    prod_id=request.GET["prod_id"]
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    cart_product=Cart.objects.filter(user=request.user)
    overallcost=0
    shippingcost=70
    total_qty=0
    for p in cart_product:
        temp_cost= p.quantity * p.product.discounted_price
        overallcost += temp_cost
        total_qty += p.quantity
    total_cost=overallcost + shippingcost
    data={"amount":overallcost,
        "totalamount":total_cost,
        "total_qty":total_qty}
    return JsonResponse(data)

@login_required
def minus_cart(request):
    prod_id=request.GET["prod_id"]
    cart=Cart.objects.get(Q(product=prod_id) & Q(user=request.user) )
    if cart:
        cart.quantity-=1
        cart.save()

    if cart.quantity != 0:   
        cart_product=Cart.objects.filter(user=request.user)
        overallcost=0
        shippingcost=70
        total_qty=0
        for p in cart_product:
            temp_cost= p.quantity * p.product.discounted_price
            overallcost += temp_cost
            total_qty += p.quantity
        total_cost=overallcost + shippingcost
        data={"amount":overallcost,
            "totalamount":total_cost,
            "total_qty":total_qty}
        return JsonResponse(data)
@login_required
def delete_cart(request):
    prod_id=request.GET["prod_id"]
    cart=Cart.objects.get(Q(product=prod_id) & Q(user=request.user) )
    cart.delete()
    cart_product=Cart.objects.filter(user=request.user)
    overallcost=0
    shippingcost=70
    total_qty=0
    for p in cart_product:
        temp_cost= p.quantity * p.product.discounted_price
        overallcost += temp_cost
        total_qty += p.quantity
    total_cost=overallcost + shippingcost
    data={"amount":overallcost,
        "totalamount":total_cost,
        "total_qty":total_qty}
    return JsonResponse(data)