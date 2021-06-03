from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
import datetime

from .forms import ContacoForm
from .models import contacto

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
    return render(request, 'website/imformation.html')
def contact_page_view(request):
    context = {'contactos': contacto.objects.all()}
    return render(request, 'website/contact.html',context)
def quiz_page_view(request):
    return render(request, 'website/quizz.html')
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




