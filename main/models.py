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

class Transactions(models.Model):
    sender_card = models.ForeignKey(BankCard,related_name='sent_transactions', on_delete=models.CASCADE)
    receiver_card = models.ForeignKey(BankAccount,related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2,default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=[
        ('success', 'Success'),
        ('failed', 'Failed'),
    ])
    def __str__(self):
        return f"{self.amount} transferred from {self.sender_card.card_number} to {self.receiver_card.card_number} on {self.timestamp}"