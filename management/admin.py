from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(products)
admin.site.register(locations)
admin.site.register(movements)