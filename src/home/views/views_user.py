import json
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

def login_view(request: HttpRequest):

    # verifica se o user esta logado
    if request.user.is_authenticated:
        return redirect('home:resume')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # tenta logar o user
        user = authenticate(request, username=username, password=password)

        # verifica se o user foi logado
        if user is not None:
            login(request, user)
            return redirect('home:resume')
        else:
            return render(request, 'home/pages/login.html', {'error': 'Credenciais inválidas'})
        

    return render(request, 'home/pages/login.html')


def logout_view(request):
    '''
    Função para deslogar o usurario
    '''

    # verifica se o usuario esta logado
    if not request.user.is_authenticated:
        return redirect('home:resume')

    logout(request) # desloga o usuario
    return redirect('home:resume') # redireciona para a home

def exclude_user(request: HttpRequest):
    '''
    Função para excluir o usuario

    Atenção:
        A função so funciona se o user estiver logado
        Depois de excluir o usuario não será possivel recupera-lo
    '''

    # verifica se o user esta logado
    if not request.user.is_authenticated:
        return redirect('home:resume')
    
    # exclui o usurario
    request.user.delete()

    # redireciona para a home
    return redirect('home:resume')


def register_view(request: HttpRequest):
    '''
    Função para registrar o usuario usando usercreationform
    '''

    # verifica se o user esta logado
    if request.user.is_authenticated:
        return redirect('home:resume')
    
    # verifica se o request e post
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # cria o formulario

        # verifica se o formulario e valido
        if form.is_valid():
            user = form.save() # salva o formulario
            login(request, user)  # loga o user
            return redirect('home:resume') # redireciona para a home
        else:
            # se o formulario nao for valido mostra o erro no template
            return render(request, 'home/pages/register.html', {'error': form.errors})

    # se nao for post redireciona para o template
    return render(request, 'home/pages/register.html')

def callback_google(request: HttpRequest):
    if not (request.method == 'POST'):
        return JsonResponse({'error': "Metodo nao permitido"}, status=405)
    
    try:
        body = json.loads(request.body)
        token = body.get('token')
    
        if not token:
            return JsonResponse({'error': "Token nao encontrado"}, status=400)
        
        # valida o token do google
        id_info = id_token.verify_oauth2_token(token, google_requests.Request(), '1011975736026-t18s4p91b8hbl12t78mu445nlblbqevi.apps.googleusercontent.com')

        #pegando as informações do usuario
        email = id_info.get('email')
        name = id_info.get('name')

        # criando o usuario
        user, created = User.objects.get_or_create(email=email, defaults={'username': email.split('@')[0],'first_name': name.strip()})

        # logando o usuario
        login(request, user)

    except ValueError:
        return JsonResponse({'error': "Token invalido"}, status=400)

    return redirect('home:resume')


