from django.contrib import admin
from .models import PunWordEn,PunWordRu

# Register your models here.
admin.site.register([
    PunWordEn,
    PunWordRu,
    ])