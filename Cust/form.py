from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django import forms

class CustomerRegistrationform(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email=forms.EmailField(required=True,label="Email address",widget=forms.EmailInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput( attrs={"class":"form-control"}),
        }

class Customerloginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}))
    password = forms.CharField(label=("Password"),strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
    )

class Customerpasswform(PasswordChangeForm):
        old_password = forms.CharField(label=("Old password"),strip=False,
                                    widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                        "autofocus": True,
                                                                        "class":"form-control"}) )
        new_password1 = forms.CharField(label=("New password"),strip=False,
                                    widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                        "autofocus": True,
                                                                        "class":"form-control"}) )
        new_password2 = forms.CharField(label=("Confirm password"),strip=False,
                                    widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                        "autofocus": True,
                                                                        "class":"form-control"}) )
class CustomerProfileform(forms.ModelForm):
    class Meta:
        model=Customers
        fields=["name","locality","city","state","zipcode",]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "locality":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "state":forms.Select(attrs={"class":"form-control"}),
            "zipcode":forms.NumberInput(attrs={"class":"form-control"})
        }
