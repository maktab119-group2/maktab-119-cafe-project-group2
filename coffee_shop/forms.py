from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'category', 'discount', 'description', 'serving_time_period',
                  'estimated_cooking_time', 'image']
