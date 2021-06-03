from django.db import migrations, models
import django.db.models.deletion


class Utilizador (models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.FileField(upload_to='email/%Y/%m/%d/')


class contacto (models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField(max_length = 65)
    mensagem = models.TextField(max_length=2000)

    def __str__(self):
        return self.mensagem[:30]
class quizz (models.Model):
    primeira = models.CheckConstraint
    segunda