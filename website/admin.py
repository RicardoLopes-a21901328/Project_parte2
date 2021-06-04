from django.contrib import admin

from .models import Utilizador
from .models import contacto
from .models import quizz

admin.site.register(Utilizador)
admin.site.register(contacto)
admin.site.register(quizz)