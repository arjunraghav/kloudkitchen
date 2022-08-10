from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from acnt.models import VendorProfile

User = get_user_model()

# Create your models here.
MENU_TYPE = (('BREAKFAST', 'Breakfast'),
             ('LUNCH', 'Lunch'),
             ('DINNER', 'Dinner'),)


class Cuisine(models.Model):
    title = models.CharField(max_length=150, help_text=_("Title of the Cuisine, Like 'North Indian', 'South Indian'."),
                             unique=True)
    details = models.TextField(max_length=3000, blank=True, help_text=_("Enter the details."))
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']


class DishCategory(models.Model):
    title = models.CharField(max_length=150, help_text=_("Title of the Dish Category, like 'Idli', 'Dosa'."),
                             unique=True)
    details = models.TextField(max_length=3000, blank=True, help_text=_("Enter the details."))
    created_at = models.DateField(auto_now_add=True, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='dish_category')

    def __str__(self):
        return f"{self.cuisine.title}-{self.title}"

    class Meta:
        ordering = ['title']


class Dish(models.Model):
    dish_category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dish')
    title = models.CharField(max_length=150, help_text=_("Title of the Dish Category."), unique=True)
    details = models.TextField(max_length=3000, blank=True, help_text=_("Enter the details."))
    created_at = models.DateField(auto_now_add=True, null=True)

    # vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='dish')

    def __str__(self):
        return f"{self.dish_category.title}-{self.title}"

    # class Meta:
    #     ordering = ['dish_category']


class VendorMenuId(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_menu_id')
    menu_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, null=True)
    menu_type = models.CharField(choices=MENU_TYPE, max_length=10, help_text=_("Select menu type."), null=True)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='vendor_menu_id')

    def __str__(self):
        return f'{self.vendor.est_name}_{self.menu_id}'


class VendorMenu(models.Model):
    vendor_menu_id = models.ForeignKey(VendorMenuId, on_delete=models.CASCADE, related_name='vendor_menu')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='vendor_menu')
    price = models.PositiveSmallIntegerField(help_text=_("Price."), null=True)

    def __str__(self):
        return self.dish.title


class CustomerMenu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_menu')
    menu_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, null=True)
    menu_type = models.CharField(choices=MENU_TYPE, max_length=10, help_text=_("Select menu type."), null=True)
    vendor_menu = models.ForeignKey(VendorMenu, on_delete=models.CASCADE, related_name='customer_menu')

    def __str__(self):
        return f'{self.user}-{self.menu_id}'
