from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login_django(request, user)
            return HttpResponse("<p>Login realizado com sucesso!</p>")
        else:
            return HttpResponse("<p>Credenciais inválidas. Tente novamente.</p>")
def home_view(request):
    return HttpResponse("<p>Olá, sou o Pedro e essa é a página de login do usuário!</p")

def login(request):
    return render(request, 'usuarios/login.hmtl')

