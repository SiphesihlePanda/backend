from dataclasses import field
from venv import create
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ["username","email",'password1','password2']

