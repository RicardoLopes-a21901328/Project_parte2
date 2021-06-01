from django.shortcuts import render
import datetime

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
    return render(request, 'website/contact.html')
def quiz_page_view(request):
    return render(request, 'website/quizz.html')





