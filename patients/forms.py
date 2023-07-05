from django import forms
from django.contrib.auth.forms import UserCreationForm
from patients.models import User
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    
    class Meta:
        model = User
        fields= ['email', 'username', 'full_name', 'password1', 'password2']
        
        
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = {'email', 'password'}
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login')