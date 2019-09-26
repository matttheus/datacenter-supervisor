from django.contrib import admin
from .models import Temperature, Gas, Humidity

# Register your models here.

adm_models = [ Temperature, Gas, Humidity ]
admin.site.register(adm_models)