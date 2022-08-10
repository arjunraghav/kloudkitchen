from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cuisine)
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(VendorMenuId)
admin.site.register(VendorMenu)
admin.site.register(CustomerMenu)