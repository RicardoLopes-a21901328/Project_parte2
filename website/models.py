from django.db import migrations, models
import django.db.models.deletion

class Utilizador (models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField(max_length = 200)



class contacto (models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField(max_length=200)
    mensagem = models.CharField(max_length=2000)


