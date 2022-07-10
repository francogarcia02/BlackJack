from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {'fields': ('username','password')}),)

admin.site.register(Profile)
# Register your models here.
