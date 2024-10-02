from django.shortcuts import render,redirect
from .forms import CreateAccountFrom
from django.db import IntegrityError
from .models import BankAccount
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
        return render(request, 'main/home.html')
    else:
        return render(request,'main/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main-page')
    if request.method =='POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Login successfull")
                return redirect('main-page')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form':form})


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

def log_out(request):
    logout(request)
    return redirect('main-page')