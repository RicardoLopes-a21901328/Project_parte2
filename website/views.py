from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
import datetime
from .forms import ContacoForm
from .models import contacto
from .models import quizz


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)
def login_page_view(request):
    return render(request, 'website/Login.html')
def media_page_view(request):
    return render(request, 'website/media.html')
def raids_page_view(request):
    return render(request, 'website/raids.html')
def religion_page_view(request):
    return render(request, 'website/religion.html')
def war_page_view(request):
    return render(request, 'website/war.html')
def comments_page_view(request):
    return render(request, 'website/Comments.html')
def information_page_view(request):
    return render(request, 'website/information.html')
def quiz_page_view(request):
    return render(request, 'website/quizz.html')

def contact_page_view(request):
    context = {'contactos': contacto.objects.all()}
    return render(request, 'website/Contact.html',context)

def ver_user(request, contact_name):
    return render(request, 'website/user.html')

def novocontact_page_view(request):
    form = ContacoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contact'))

    context = {'form': form}
    return render(request, 'website/novocontacto.html',context)

def editar_page_view(request, contacto_id):

    contato = contacto.objects.get(pk=contacto_id)
    form = ContacoForm(request.POST or None, instance = contato)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contact'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/editarcontacto.html',context)

def apaga_contacto_view(request, contacto_id):
    contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('contact'))

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
                    request,
                    username=username,
                    password=password,

        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('contact'))
        else:
            return render(request, 'website/Login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'website/Login.html')


def logout_view(request):
    logout(request)
    return render(request, 'website/Login.html', {
        'message': 'Logged out'})

def quizz_result(request):

    form = ContacoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('quizzresult'))

    context = {'form': form, 'quizz_id': quizz.total}
    if request.method == "post":
        primeira = request.method["opinion1"].value
        segunda = request.method["opinion2"].value
        terceira = request.method["opinion3"].value
        quarta = request.method["opinion4"].value
        quinta = request.method["opinion5"].value
        sexta = request.method["opinion6"].value
        setima = request.method["opinion7"].value
        oitava = request.method["opinion8"].value
        nona = request.method["opinion9"].value
        decima = request.method["opinion10"].value

        if primeira !="1" or primeira == None:
            quizz.primeira = 0
        else:
            quizz.primeira = 1

        if segunda !="1" or segunda == None:
            quizz.segunda = 0
        else:
            quizz.segunda = 1

        if terceira !="1" or terceira == None:
            quizz.terceira = 0
        else:
            quizz.terceira = 1

        if quinta !="1" or quinta == None:
            quizz.quinta = 0
        else:
            quizz.quinta = 1

        if sexta !="1" or sexta == None:
            quizz.sexta = 0
        else:
            quizz.sexta = 1

        if setima !="1" or setima == None:
            quizz.setima = 0
        else:
            quizz.setima = 1

        if oitava != "1" or oitava == None:
            quizz.oitava = 0
        else:
            quizz.oitava = 1

        if nona != "1" or nona == None:
            quizz.nona = 0
        else:
            quizz.nona = 1

        if decima != "1" or decima == None:
            quizz.decima = 0
        else:
            quizz.decima = 1

        if quarta != 700 or quarta== None:
            quizz.quarta = 0
        else:
            quizz.quarta = 1

        quizz.total = quizz.primeira + quizz.segunda + quizz.terceira + quizz.quarta + quizz.quinta + quizz.sexta + quizz.oitava + quizz.setima + quizz.nona + quizz.decima

    return render(request, 'website/quizz.html', {'message': {quizz.total}})
