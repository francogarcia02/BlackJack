from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    email = forms.EmailField(required=True ,widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    password1 = forms.CharField(label='Contraaseña     ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','nombre','apellido','email','password1','password2']
        help_texts = {
            "username": None
        }
