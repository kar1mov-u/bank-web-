from django import forms

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