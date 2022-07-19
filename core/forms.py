from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label='Apellido', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    address = forms.CharField(label='Direccion', required=True, widget=forms.TextInput(attrs={'placeholder': 'address'}))
    email = forms.EmailField(label='Correo electronico', required=True ,widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    password1 = forms.CharField(label='Contraaseña     ', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','address','email','password1','password2']
        help_texts = {
            "username": None
        }
