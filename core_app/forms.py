from django import forms
from core_app.models import *


class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = ('title', 'details')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'title', 'placeholder': 'Title'}),
            'details': forms.Textarea(
                attrs={'class': 'form-control', 'type': 'textarea', 'rows': 4, 'cols': 30, 'name': 'details',
                       'placeholder': 'Details about the cuisine'}),
        }


class DishCatForm(forms.ModelForm):
    class Meta:
        model = DishCategory
        fields = ('title', 'details', 'cuisine')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'title', 'placeholder': 'Title'}),
            'details': forms.Textarea(
                attrs={'class': 'form-control', 'type': 'textarea', 'rows': 4, 'cols': 30, 'name': 'details',
                       'placeholder': 'Details about the dish category'}),
            # 'cuisine': forms.ChoiceField(
            #     attrs = {'class': 'form-control', 'type': 'input', 'name': 'title', 'placeholder': 'Title'}),
        }


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('title', 'details', 'dish_category')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'input', 'name': 'title', 'placeholder': 'Title'}),
            'details': forms.Textarea(
                attrs={'class': 'form-control', 'type': 'textarea', 'rows': 4, 'cols': 30, 'name': 'details',
                       'placeholder': 'Details about the dish'}),
            # 'dish_category': forms.ChoiceField(
            #     attrs = {'class': 'form-control', 'type': 'input', 'name': 'title', 'placeholder': 'Title'}),
        }


class VendorMenuIdForm(forms.ModelForm):
    class Meta:
        model = VendorMenuId
        fields = "__all__"


class VendorMenuForm(forms.ModelForm):
    class Meta:
        model = VendorMenu
        fields = "__all__"
