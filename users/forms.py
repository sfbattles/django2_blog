from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_access = forms.ChoiceField

    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email','password1','password2']
