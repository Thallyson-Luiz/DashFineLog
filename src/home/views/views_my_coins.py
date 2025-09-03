from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from home.models import CriptoMoeda, Coin
from modules.coins import config_coin_today
from django.contrib.auth.decorators import login_required



@login_required(login_url='home:login')
def my_coins(request: HttpRequest):
    # pega o user ativo
    user = request.user
    


    # pega as moedas
    try:
        coins = user.coins.all() # type: ignore | o vscode não consegue detectar que o user tem o atributo coins, algo normal em IDES, pois ele foi criado no model coin
    except:
        coins = list() # se o user nao tiver moedas, retorna uma lista 

    # trata os dados
    COINS_INFO = config_coin_today(coins) # em caso de erro retorna uma lista vazia

    # verifica se houve erros
    error = '' 
    if request.GET.get('error') == '1':
        error = 'Erro ao criar moeda, verifique se o ticker e trading pair são aceitos pelo awesome e tente novamente'

    # contexto para enviar os dados para o template
    context = {
        'coins': COINS_INFO,
        'error': error
    }


    return render(request, 'home/pages/my_coins.html', context)

@login_required(login_url='home:login')
def exclude_coin(request: HttpRequest, coinname: str):
    '''
    função para excluir uma moeda do template coins

    Argumentos:
        coinname: str

    Atenção:
        A função so funciona se o user estiver logado
        Depois de excluir a moeda nao sera possivel recupera-la
    '''

    # pega o user ativo
    USER = request.user

    # tratando coiname
    TICKER, TRADING_PAIR  = coinname.split('-')

    # pega a moeda
    try:
        COIN = USER.coins.filter(ticker=TICKER, trading_pair=TRADING_PAIR) # type: ignore | o vscode não detecta que o user tem o atributo coins, algo normal em IDES, pois ele foi criado no model coin
    except:
        # se nao for encontrada a moeda, redireciona para a home
        return redirect('home:home')

    # exclui a moeda
    COIN.delete()

    return redirect('home:my-coins')

@login_required(login_url='home:login')
def add_coin(request: HttpRequest, ticker: str, trading_pair: str):
    '''
    Função para vincular uma moeda ao usuario logado

    Argumentos:
        ticker: str
        trading_pair: str

    Atenção:
        A função so funciona se o user estiver logado
        caso o ticker seja invalido o usuario não conseguira vincular a moeda e sera redirecionado para a home
    '''

    # trata os dados recebidos
    ticker = ticker.upper().strip()
    trading_pair = trading_pair.upper().strip()


    # pega o user ativo
    USER = request.user
    url = reverse('home:my-coins')
    # cria a moeda
    try:
        Coin.objects.create(ticker=ticker, trading_pair=trading_pair, User_person=USER)
    except:
        # se nao for possivel criar a moeda, adiciona um erro
        url += '?error=1'

    # redireciona para a home
    return redirect(url)
