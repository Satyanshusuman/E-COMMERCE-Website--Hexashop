from django.shortcuts import render,redirect
from django.views import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationform()
        return render(request,"cust/registartion.html",{"form":form})
    
    def post(self,request):
        form=CustomerRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations!!!  Registered sucessfully..")
        
        return render(request,"cust/registartion.html",{"form":form})
    
class CustomerSignin(View):
    def get(self,request):
        form=Customerloginform()
        return render (request,"cust/login.html",{"form":form})
    
    def post(self,request):
        form=Customerloginform(request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            psw=form.cleaned_data["password"]
            user=authenticate(username=uname,password=psw)
            if user is not None and user.is_active :
                login(request,user)
                # messages.success(request,"Logged in successfully!!")
                return redirect("/")
        else:
            messages.error(request,"Login with valid Credentials!!")    
            return render (request,"cust/login.html",{"form":form})

@method_decorator(login_required,name="dispatch")
class CustomerProfile(View):
    def get(self,request):
        form=CustomerProfileform()
        return render (request,"cust/profile.html",{"form":form,"active":"btn-dark"})
   
    def post(self,request):
        form=CustomerProfileform(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data["name"]
            locality=form.cleaned_data["locality"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            zipcode=form.cleaned_data["zipcode"]
            cust=Customers(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            cust.save()
            messages.success(request,"Your Profile updated sucessfully!! ")
            return redirect("/Cust/profile/")

        return render (request,"cust/profile.html",{"cust":cust,"active":"btn-dark"})

@method_decorator(login_required,name="dispatch")     
class Customerlogout(View):
    def get(self,request):
        logout(request)
        return redirect("/Cust/login")

@method_decorator(login_required,name="dispatch")    
class CustomerPasswchange(PasswordChangeView):

    def form_valid(self, form):
        messages.success(self.request,"Password changed successfully!!!")
        return super().form_valid(form)

@login_required
def customeraddress(request):
    customer=Customers.objects.filter(user=request.user)  
    return render(request,"cust/address.html",{"active":"btn-dark","customer":customer})
    