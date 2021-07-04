from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page_view, name = 'home' ),
    path('login', views.login_page_view, name='login'),
    path('user', views.login_page_view, name='user'),
    path('war', views.war_page_view, name='war'),
    path('religion', views.religion_page_view, name='religion'),
    path('raids', views.raids_page_view, name='raids'),
    path('comments', views.comments_page_view, name='comments'),
    path('media', views.media_page_view, name='media'),
    path('information', views.information_page_view, name='information'),
    path('quizz', views.quiz_page_view, name='quizz'),
    path('contact', views.contact_page_view, name='contact'),
    path('novocontacto', views.novocontact_page_view, name='novocontacto'),
    path('editarco/<int:contacto_id>', views.editar_page_view, name='editarco'),
    path('apaga/<int:contacto_id>', views.apaga_contacto_view, name='delete'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('quizzre', views.quizz_result, name='quizzresult')
]