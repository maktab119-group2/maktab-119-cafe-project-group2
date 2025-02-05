from django import forms
from coffee_shop.models import *


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400'
        })
    )


# class OrderUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['status']
#         widgets = {
#             'status': forms.Select(choices=[
#                 ('pending', 'Pending'),
#                 ('preparing', 'Preparing'),
#                 ('ready', 'Ready'),
#                 ('completed', 'Completed')
#             ])
#         }


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'category', 'discount', 'description', 'serving_time_period',
                  'estimated_cooking_time', 'image']
