from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', CustomerRegistration.as_view()),
    path("login/",CustomerSignin.as_view()),
    path("profile/",CustomerProfile.as_view()),
    path("logout/",Customerlogout.as_view()),
    path("passwchange/",CustomerPasswchange.as_view(template_name="cust/password.html",
                                                         form_class=Customerpasswform,
                                                         success_url="/Cust/profile/")),
    path("address/",customeraddress)]