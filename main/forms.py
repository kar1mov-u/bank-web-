from django import forms
from .models import BankAccount,BankCard

class CreateAccountFrom(forms.Form):
    username = forms.CharField( max_length=150, required=True, label ='Username')
    email = forms.EmailField( required=False,label='Email')
    password = forms.CharField( widget=forms.PasswordInput, required=True, label = 'Password')
    confirm_password = forms.CharField(widget= forms.PasswordInput, required=True, label = 'Confirm Password')
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data .get('password')
        confirm_password= cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
    
from django import forms

class AddCard(forms.Form):
    card_number = forms.CharField(
        max_length=16,
        label="Card Number",
        widget=forms.TextInput(attrs={'placeholder': 'Card Number', 'pattern': '\d{16}', 'title': '16-digit card number'})
    )
    balance = forms.DecimalField(
        max_digits=15,
        decimal_places=2,
        label="Balance",
        widget=forms.NumberInput(attrs={'placeholder': 'Balance'})
    )

class TrasnferForm(forms.Form):
    
    sender = forms.ChoiceField(
        label = "Select Sender Card",
        choices =[]
    )
    reciever = forms.CharField(
        max_length=16,
        label="Card Number",
        widget=forms.TextInput(attrs={'placeholder': 'Card Number', 'pattern': '\d{16}', 'title': '16-digit card number'})
    )
    amount = forms.DecimalField(
        max_digits=15,
        decimal_places=2,
        label="Amount",
        widget=forms.NumberInput(attrs={'placeholder': 'Amount'})
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super(TrasnferForm,self).__init__(*args,**kwargs)
        if user:
            cards = BankCard.objects.filter(owner__user=user)
            self.fields['sender'].choices = [(card.id,f"{card.card_number}- Balance:{card.balance}")for card in cards]