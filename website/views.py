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
                    password=password
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
        return HttpResponseRedirect(reverse('quizz'))

    if request.method == "post":
        quizz.primeira = request.method["opinion1"].
        quizz.segunda = request.method["opinion2"].value
        quizz.terceira = request.method["opinion3"].value
        quizz.quarta = request.method["opinion4"].value
        quizz.quinta = request.method["opinion5"].value
        quizz.sexta = request.method["opinion6"].value
        quizz.setima = request.method["opinion7"].value
        quizz.oitava = request.method["opinion8"].value
        quizz.nona = request.method["opinion9"].value
        quizz.decima = request.method["opinion10"].value

        if quizz.primeira != '1' and quizz.primeira == '':
            primeira = 0
        else:
            primeira = 1

        if quizz.segunda != '1' and quizz.segunda == '':
            segunda = 0
        else:
            segunda = 1

        if quizz.terceira != '1' and quizz.terceira == '':
            terceira = 0
        else:
            terceira = 1

        if quizz.quinta != '1':
            quinta = 0
        else:
            quinta = 1

        if quizz.sexta != '1':
            sexta = 0
        else:
            sexta = 1

        if quizz.setima != '1':
            setima = 0
        else:
            setima = 1

        if quizz.oitava != '1':
            oitava = 0
        else:
            oitava = 1

        if quizz.nona != '1':
            nona = 0
        else:
            nona = 1

        if quizz.decima != '1':
            decima = 0
        else:
            decima = 1

        if quizz.quarta != 700:
            quarta = 0
        else:
            quarta = 1
        quizz.total = primeira + segunda + terceira + quarta + quinta + sexta + oitava + setima + nona + decima

        return render(request, 'website/quizz.html',{'message':{quizz.total}})
