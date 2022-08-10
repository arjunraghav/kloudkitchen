from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter your email address',
        widget=forms.TextInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        # help_text='Enter First Name',
        widget=forms.TextInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        # help_text='Enter Last Name',
        widget=forms.TextInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter a unique username',
        widget=forms.TextInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter a Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Password Again'}),
    )

    # customer_type = forms.ChoiceField(help_text='Check this box if you are a vendor')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'customer_type'
        ]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter your username',
        widget=forms.TextInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Username'}),
    )

    password = forms.CharField(
        help_text='Enter your Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'style': 'border-radius: 12px;box-shadow: 3px 3px 9px;border-style: none;margin-top: 4px;margin-right: 0px;margin-bottom: 4px;text-align: left;padding-left: 12px;padding-right: 2px;',
            'placeholder': 'Password'}),
    )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('phone_number', 'about', 'date_of_birth', 'address', 'pincode')

        widgets = {
            'phone_number': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'phone', 'placeholder': 'Phone number'}),
            'about': forms.Textarea(
                attrs={'class': 'form-control', 'type': 'textarea', 'rows': 4, 'cols': 30, 'name': 'about', 'placeholder': 'About'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'name': 'dob', 'placeholder': 'DOB'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'address', 'placeholder': 'Address'}),
            'pincode': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'pincode', 'placeholder': 'Pincode'}),
        }
