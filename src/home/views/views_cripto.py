from django.shortcuts import render, redirect
from django.http import HttpRequest
from home.models import CriptoMoeda, Coin
from modules.cripto import get_bitcoin_today, config_cripto_today, get_market_humor


def cripto(request: HttpRequest):
    '''
    Função para renderizar o template de cripto
    trata os dados e envia para o template cripto
    '''


    # obtendo e tratando os dados
    CRIPTOS = CriptoMoeda.objects.all() # pega todas as criptomoedas
    CRIPTO_INFO = config_cripto_today(CRIPTOS) # trata os dados
    MARKET_HUMOR = get_market_humor() # pega o humor do mercado

    # envia os dados para o template
    context ={
        'criptos': CRIPTO_INFO,
        'market_humor': MARKET_HUMOR
    }

    return render(request, 'home/pages/cripto.html', context)
