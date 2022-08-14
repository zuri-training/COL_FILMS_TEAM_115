from enum import unique
from tabnanny import verbose
from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from .models import Contact, Profile
  
class CustomUserCreationForm(UserCreationForm):  
    firstname = forms.CharField(label='First Name', min_length=2, max_length=150)  
    lastname = forms.CharField(label='Last Name', min_length=2, max_length=120)  
    username = forms.CharField(label='Username', min_length=2, max_length=150)  
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def clean_email(self):  
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return email
        # new = User.objects.filter(email = email)  
        # if new.count():  
        #     raise ValidationError(" Email Already Exist")  
        # return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'student_id_card')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
