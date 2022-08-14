from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import uuid
from .managers import CustomUserManager

# Create your models here.

CITY = (('BANGALORE', 'BANGALORE'),
        ('MYSORE', 'MYSORE'))
TYPE = (('RESTO', 'Restaurants/Hotel/Canteen'),
        ('CATER', 'Caterers'))
RATE = ((1, '1-Bad'),
        (2, '2-Average'),
        (3, '3-Good'),
        (4, '4-Very good'),
        (5, '5-Excellent'))
USER_TYPE = (('C', 'CUSTOMER'),
             ('V', 'VENDOR'),
             ('A', 'ADMIN'))


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("Email address"), unique=True)
    customer_type = models.CharField(max_length=1, choices=USER_TYPE,
                                     blank=False, null=False,
                                     help_text=_("Are you a vendor?"))

    # slug = models.SlugField(null=True, blank=True)

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def get_vendor_est_name(self):
        if self.customer_type == 'V':
            return self.vendor_profile.est_name
        else:
            return "Customer"

    # def save(self, *args, **kwargs):
    #     if self.customer_type == 'C':
    #         group = Group.objects.get(name=self.customer_type)
    #         self.groups.add(group)
    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.username)
    #     super(CustomUser, self).save(*args, **kwargs)


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile', null=True)
    phone_number = models.DecimalField(help_text=_("Enter your 10 digit phone number with country code"), max_digits=12,
                                       decimal_places=0, null=True)
    about = models.TextField(help_text=_("About yourself."))
    date_of_birth = models.DateField(help_text=_("Date of birth."), null=True)
    address = models.CharField(max_length=250, help_text=_("Enter your street address."), null=True)
    city = models.CharField(choices=CITY, max_length=20, help_text=_("Select your city."), null=True)
    pincode = models.DecimalField(decimal_places=0, max_digits=6, help_text=_("Pincode."), null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user.username)
        super(CustomerProfile, self).save(*args, **kwargs)


class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor_profile', null=True)
    est_name = models.CharField(max_length=250, help_text=_("Name of the Restaurants/Hotel/Canteen or Caterers."),
                                null=True)
    phone_number = models.DecimalField(help_text=_("Enter your 10 digit phone number with country code"), max_digits=12,
                                       decimal_places=0, null=True)
    business_phone_number = models.DecimalField(
        help_text=_("Enter your 10 digit business contact number with country code"), max_digits=12, decimal_places=0,
        null=True)
    type = models.CharField(choices=TYPE, null=True, max_length=10)
    about = models.TextField(help_text=_("About your restaurant."), null=True)
    address = models.CharField(max_length=250, help_text=_("Street address of the restaurant/organization."), null=True)
    city = models.CharField(choices=CITY, null=True, max_length=20, help_text=_("Select your city."))
    pincode = models.DecimalField(decimal_places=0, max_digits=6, help_text=_("Pincode."), null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user.username)
        super(VendorProfile, self).save(*args, **kwargs)


class Review(models.Model):
    title = models.CharField(max_length=150, help_text=_("Try some title which users can relate to your review."))
    details = models.TextField(max_length=3000, blank=True, help_text=_("Enter the detailed review."))
    rate = models.PositiveSmallIntegerField(choices=RATE, blank=True, help_text=_("Rate the Vendor."))
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='review')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} rated {self.vendor}"


class Like(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liker')
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} likes {self.vendor}"


class Following(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='following')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Followers')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is following {self.vendor}"


class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    wallet_number = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}-{self.wallet_number}"


class Coupon(models.Model):
    coupon_number = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, null=False, blank=False, help_text=_("Coupon title"))
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.coupon_number}-{self.title}"


class Testimonial(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, help_text=_("Title of the testimonials."))
    details = models.TextField(max_length=3000, blank=True, help_text=_("Enter the details."))
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.title}"

    class Meta:
        ordering = ['-created_at']

    @staticmethod
    def get_latest_3_testimonial():
        result = Testimonial.objects.all()[0:3]
        testimonial = []
        for item in result:
            testimonial.append({
                'name': f'{item.user.first_name} {item.user.last_name}',
                'user': f'{item.user.get_vendor_est_name}',
                'details': f'{item.details}',
            })
        return testimonial
