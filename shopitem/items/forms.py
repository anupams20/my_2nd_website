
from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Itemlist
from django.contrib.auth.forms import PasswordChangeForm
class Userform(forms.Form):
    email=forms.EmailField()
    password =forms.CharField(widget=forms.PasswordInput())
    confirm_password= forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data =super().clean()
        password=cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password :
            raise forms.ValidationError("password not match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=12)
    place = forms.CharField(max_length=30)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class ShoppingItemForm (forms.ModelForm):
    class Meta:
        model=Itemlist
        fields=['name', 'price', 'discount']
    
class changepass(PasswordChangeForm):
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput())
    new_password2=forms.CharField(label='Confirm New password',widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data= super().clean()
        new_password1= cleaned_data.get('new_password1')
        new_password2= cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("password do not match")
        
        return cleaned_data
