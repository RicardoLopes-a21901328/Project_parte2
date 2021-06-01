from django.contrib import admin

from .models import Utilizador
from .models import contacto

admin.site.register(Utilizador)
admin.site.register(contacto)