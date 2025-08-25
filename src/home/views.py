from django.shortcuts import render
from modules.dolar import get_dolar_today
from utils.convert import convert_float
from modules.dolar import calc_coin_variation
from modules.bitcoin import get_bitcoin_today
from utils.formate import formatar_numero
from modules.pib import get_pib_last_months
from utils.calc_variation import calc_variation_percent

# Create your views here.


def index(request):
    '''
    Função para renderizar o template de resume
    
    trata os dados e envia para o template resume
    '''

    # pega a cotação do dolar e converte para float
    DOLAR_API = get_dolar_today() # requisição do awesomeapi
    price_dolar = DOLAR_API['bid']
    price_dolar = convert_float(price_dolar)

    # pega a a varição do dolar no intervalo de 1 dia e converte para float
    dolar_price_add = DOLAR_API['varBid']
    dolar_price_add = convert_float(dolar_price_add)

    # calcula a variação percentual
    DOLAR_PERCENTAGE = calc_coin_variation(price_dolar, dolar_price_add)

# ____________________________________________________________________________________________________________________________________

    # pega a cotação do bitcoin e converte para float
    BITCOIN_API = get_bitcoin_today() # requisição do awesomeapi
    price_bitcoin = BITCOIN_API['bid']
    price_bitcoin = convert_float(price_bitcoin)
    PRICE_BITCOIN_BEFORE = price_bitcoin # armazena a cotação do bitcoin para calcular a variação
    price_bitcoin = formatar_numero(price_bitcoin)

    # pega a a varição do bitcoin no intervalo de 1 dia e converte para float
    bitcoin_price_add = BITCOIN_API['varBid']
    bitcoin_price_add = convert_float(bitcoin_price_add)

    # calcula a variação percentual
    BITCOIN_PERCENTAGE = calc_coin_variation(PRICE_BITCOIN_BEFORE, bitcoin_price_add)

    pib_old, pib_new = get_pib_last_months(2) # requisição do gov.br
    DATE_PIB = pib_new['data'] # pega a data do pib
    PIB_NEW_VALUE = pib_new['valor'] # pega o valor do pib
    pib_old = convert_float(pib_old['valor']) # converte valor antigo para float
    pib_new = convert_float(pib_new['valor']) # converte valor novo para float
    VARIATION_PIB = calc_variation_percent(pib_new, pib_old) # calcula a variacao percentual

    # envia os dados para o template
    context = {
        'dolar_today': round(price_dolar, 2),
        'dolar_variation': DOLAR_PERCENTAGE,
        'bitcoin_today': price_bitcoin,
        'bitcoin_variation': BITCOIN_PERCENTAGE,
        'pib': PIB_NEW_VALUE,
        'date_pib': DATE_PIB,
        'variation_pib': VARIATION_PIB
    }

    return render(request, 'home/pages/resume.html', context)

