from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer

# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True 
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            #create user accounts
            user = User.objects.create_user(
                username = username,
                password = password,
                email =email
            )
            #creates customer account
            customer = Customer.objects.create(
                name=username,
                user = user,
                phone = phone,
                address = address

            )
            success_msg = "User registered successfully"
            messages.success(request,success_msg)
            
        except Exception as e:
            error_msg = "Username already exists"
            messages.error(request,error_msg)
    if request.POST and 'login' in request.POST:
        context['register']=False 
                   
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid user credentials")


        
        

    return render(request, 'account.html',context)
