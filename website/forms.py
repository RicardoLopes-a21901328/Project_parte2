from django.forms import ModelForm

from .models import contacto
from .models import quizz


class ContacoForm(ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'

class QuizzForm(ModelForm):
    class Meta:
        model = quizz
        fields = '__all__'
