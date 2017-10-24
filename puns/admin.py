from django.contrib import admin
from .models import PunWord, Type

# Register your models here.
admin.site.register([
    PunWord,
    Type
    ])