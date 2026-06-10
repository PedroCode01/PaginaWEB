from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('base/', views.base, name = 'base'),
    path('home/', views.home, name = 'home'),
    path('lancar_notas/', views.lancar_notas, name = 'lancar_notas'),
]
