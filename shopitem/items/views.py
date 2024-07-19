from typing import Any
from django.shortcuts import render, redirect
from .models import Itemlist
from django.forms import formset_factory, modelformset_factory
from .forms import Userform , UserInfoForm
from .forms import LoginForm ,ShoppingItemForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .decorators import superuser_required
#from django.contrib.auth.forms import PasswordChangeForm
from .forms import changepass
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from rest_framework.decorators import api_view
from .serilizers import itemserializers
from rest_framework.response import Response
ShoppingItemFormSet=modelformset_factory(Itemlist, form=ShoppingItemForm, extra=1)

UserInfoFormSet = formset_factory(UserInfoForm, extra=1)

def post_list(request):
    items=Itemlist.objects.all()
    return render(request, 'items/item_list.html',{'items':items})

# @superuser_required
def hello(request):
    return render(request, 'items/hey_list.html')

def signup_view(request):
    if request.method == 'POST' :
        credentials_form = Userform(request.POST)
        formset = UserInfoFormSet(request.POST)

        if credentials_form.is_valid() and formset.is_valid():
            email= credentials_form.cleaned_data['email']
            password = credentials_form.cleaned_data['password']
            username = email.split('@')[0]

            user = User.objects.create_user(username=username, email=email, password=password)

            for form in formset:
                name=form.cleaned_data.get("name")
                phone_number = form.cleaned_data.get("phone_number")
                place=form.cleaned_data.get("place")

            return redirect('signup_done')
    else:
        credentials_form = Userform()
        formset = UserInfoFormSet()

    return render(request, 'items/signup.html', {
        'credentials_form': credentials_form,
        'formset': formset,
         })
    
def signup_done(request):
    return render(request, 'items/signup_done.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
          
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success_url')
            else:
                form.add_error(None, "Invalid username or password")

            
            
    else:
        form = LoginForm()
    
    return render(request, 'items/login.html', {'form': form})

def shopping_items_view(request):
    if request.method == 'POST':
        formset = ShoppingItemFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('shopping_items_done')  
    else:
        formset = ShoppingItemFormSet(queryset=Itemlist.objects.all())

    return render(request, 'items/shopping_items.html', {'formset': formset})

def shopping_items_done(request):
    return render(request, 'items/shopping_items_done.html')
def success_view(request):
    return render(request, 'items/success.html')
def logout_view(request):
    logout(request)
    return redirect('logout_done')
def logout_done(request):
    return render(request, 'items/logout_done.html')
def password_change_view(request):
    if request.method == 'POST':
        form = changepass(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change_done')
    else:
        form = changepass(request.user)
    
    return render(request, 'items/password_change.html', {'form': form})
def password_change_done(request):
    return render(request, 'items/password_change_done.html')

@api_view(['POST'])
def create(request):
    serializer= itemserializers(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def read(request):
    items=Itemlist.objects.all()
    serializer=itemserializers(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update(request,pk):
    items=Itemlist.objects.get(pk)
    serializer=itemserializers(instance=items,data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    items=Itemlist.objects.get(pk)
    items.delete()
    return Response(f'item {pk} deleted')