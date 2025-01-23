from django import forms
from .models import User
from .models import MenuItem





class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'category', 'discount', 'description', 'serving_time_period',
                  'estimated_cooking_time', 'image']
