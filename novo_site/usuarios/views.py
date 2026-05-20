from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse("<p>Olá, sou o Pedro e essa é a página de login do usuário!</p")

def login(request):
    return render(request, 'usuarios/login.hmtl')

