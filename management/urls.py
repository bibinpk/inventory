from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('locations/',addlocation),
    path('movements/',addmovement),
    path('products/',addproduct),
    path('location/<int:location_id>/',editlocation),
    path('movement/<int:movement_id>/',editmovement),
    path('product/<int:product_id>/',editproduct),
    path('locations/<int:location_id>/',deletelocation),
    path('movements/<int:movement_id>/',deletemovement),
    path('products/<int:product_id>/',deleteproduct),
]
