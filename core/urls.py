from django.urls import path
from core.views import *
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('productos/', compras, name="play"),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(template_name='social/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name="logout"),
    path('perfil/', perfil, name="perfil"),
]