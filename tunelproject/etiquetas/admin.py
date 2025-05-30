from django.contrib import admin
import data_wizard #librería
from .models import Etiqueta

# Register your models here.
admin.site.register(Etiqueta)

data_wizard.register(Etiqueta) #librería