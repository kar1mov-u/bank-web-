from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BankAccount(models.Model):
    ACCOUNT_TYPES = [
        ('savings', 'Savings'),
        ('checking', 'Checking'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20,unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2,default=0.0)
    account_type = models.CharField(max_length=15,choices=ACCOUNT_TYPES)
    data_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.account_type.capitalize()} Account"
    
class BankCard(models.Model):
    card_number = models.CharField(max_length=16,unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2,default=0.0)  
    owner = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Card number : {self.card_number}, owned by {self.owner.user.username}"