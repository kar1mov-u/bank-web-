from django.shortcuts import render,redirect
from .forms import CreateAccountFrom,AddCard
from django.db import IntegrityError
from django.db.models import Sum

from .models import BankAccount,BankCard
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user =request.user
        bank_acc = BankAccount.objects.get(user=user)
        total_balance = BankCard.objects.filter(owner=bank_acc).aggregate(total=Sum('balance'))['total'] or 0
        return render(request, 'main/home.html',{'balance':total_balance})
    else:
        return render(request,'main/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect ('main-page')
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfull")
                return redirect ('main-page')
            else:
                messages.error(request,"Incorrect Password or Username")
    else:
        form = AuthenticationForm()
    return render(request,'main/login.html',{'form':form})
                
            


def create_acc(request):
    if request.user.is_authenticated:
        return redirect('main-page')
    if request.method =='POST':
        form = CreateAccountFrom(request.POST)
        if form.is_valid():
            try:
                user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email = form.cleaned_data['email']
            )
                BankAccount.objects.create(
                    user=user,
                    account_number = "ACC"+str(user.id),
                    account_type = "savings"
                )
                messages.success(request, 'Your account has been created successfully! You can now log in.')
                return redirect('login-page')
            except IntegrityError:
                messages.error(request, "This username is already taken. Please choose another.")
                

    else:
        form = CreateAccountFrom()
        
    return render(request, 'main/create_acc.html',{'form':form})

@login_required
def profile(request):
    user = request.user
    try:
        bank_account = BankAccount.objects.get(user=user)
        bank_cards = BankCard.objects.filter(owner = bank_account)
    except BankAccount.DoesNotExist: 
        bank_account = None
        
    return render(request,'main/profile.html',{'user':user, 'bank_account':bank_account,'bank_cards':bank_cards})

@login_required
def view_cards(request):
    user = request.user
    bank_acc = BankAccount.objects.get(user=user)
    cards = BankCard.objects.filter(owner=bank_acc)
    return render(request,'main/view_cards.html',{'cards':cards})

@login_required
def add_card(request):
    if request.method =='POST':
        form = AddCard(request.POST)
        if form.is_valid():
            card_num= form.cleaned_data['card_number']
            bal = form.cleaned_data['balance']
            user = request.user
            bank_acc = BankAccount.objects.get(user=user)
            try:
                BankCard.objects.create(
                    card_number= card_num,
                    balance =  bal,
                    owner = bank_acc
                )
                messages.success(request, "New card was added successfully")
                return redirect('bank-cards-page')
                
            except IntegrityError:
                form.add_error('card_number', 'A card with this number already exists. Please use a different card number.')

        
    else:
        form = AddCard()
    return render(request,'main/add_card.html',{"form":form})

def support(request):
    return render(request,'main/support.html')

def log_out(request):
    logout(request)
    return redirect('main-page')
