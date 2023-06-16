from django.contrib import admin
from django.urls import path
from. views import *
urlpatterns = [
    path('add_to_cart/', add_cart),
    path('showcart/', showcart.as_view()),
    path('pluscart/', plus_cart),
    path('minuscart/', minus_cart),
    path('delcart/', delete_cart),
]