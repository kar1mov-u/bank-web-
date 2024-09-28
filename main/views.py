from django.shortcuts import render,redirect
from .forms import CreateAccountFrom
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def login(request):
    
    return render(request, 'main/login.html')

def create_acc(request):
    if request.method =='POST':
        form = CreateAccountFrom(request.POST)
        if form.is_valid():
            #Need to retrieve data from the form.cleaned_data and create user entry in database
            return redirect('login-page')
    else:
        form = CreateAccountFrom()
        
    return render(request, 'main/create_acc.html',{'form':form})