from django.contrib import admin

# Register your models here.
from .models import place, place2

admin.site.register(place)
admin.site.register(place2)