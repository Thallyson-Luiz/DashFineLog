from modules.dolar import get_dolar_with_days
from modules.cripto import get_bitcoin_with_days
from modules.inflation import get_ipca_last_months, get_inpc_last_months
from modules.selic import get_selic_last_months
from utils.convert import convert_float
from utils.time import get_days_week, get_months
from django.http import Http404, HttpRequest, JsonResponse
# Create your views here.

def get_dolar_for_days(request: HttpRequest, days: int=6):
    '''
    Função de api simples para enviar ao frontend as cotações do dólar 
    em relação ao real em um intervalo de dias.

    parâmetros:
        days = numero de dias para pega a cotação

    retorna:
        json com as cotações do dolar e datas
    '''

    # Valida os parâmetros
    # tambem inpõe um limite de 1 mês
    if not isinstance(days, int) or days >= 30:
        raise Http404("O parâmetro 'days' deve ser um inteiro.")

    dolar_api_days = get_dolar_with_days(days) # requisição do awesomeapi

    # 🟡 tratando os dados

    # ◻️ preço do dolar
    dolar_prices = []
    for dolar in dolar_api_days:
        price = convert_float(dolar['bid'])
        dolar_prices.append(price)

    # ◻️ datas
    days_week = get_days_week(days)

    CONTEXT = {
        'dolar_prices': dolar_prices,
        'days_week': days_week
    }

    return JsonResponse(CONTEXT)




def get_bitcoin_for_days(request: HttpRequest, days: int=5):
    '''
    Função de api simples para enviar ao frontend as cotações do bitcoin 
    em relação ao real em um intervalo de dias.

    parâmetros:
        days = numero de dias para pega a cotação

    retorna:
        json com as cotações do dolar e datas
    '''

    # Valida os parâmetros
    # tambem inpõe um limite de 1 mês
    if not isinstance(days, int) or days >= 30:
        raise Http404("O parâmetro 'days' deve ser um inteiro.")
    
    bitcoin_api_days = get_bitcoin_with_days(days) # requisição do awesomeapi
    # 🟡 tratando os dados


    # ◻️ preço do bitcoin
    bitcoin_prices = []
    for bitcoin in bitcoin_api_days:
        price = convert_float(bitcoin['bid'])
        bitcoin_prices.append(price)

    # ◻️ datas
    days_week = get_days_week(days)


    CONTEXT = {
        'bitcoin_prices': bitcoin_prices,
        'days_week': days_week
    }

    return JsonResponse(CONTEXT)



def get_ipca_for_months(request: HttpRequest, months: int=5):
    '''
    Função de api para enviar ao frontend a media do ipca
    em um intervalo de meses

    parâmetros:
        months = numero de meses para pega a media e data

    retorna:
        json com as medias do ipca e datas
    '''

    # Valida os parâmetros
    # tambem inpõe um limite de 1 mês
    if not isinstance(months, int) or months >= 30:
        raise Http404("O parâmetro 'months' deve ser um inteiro maior que 0 e menor que 31.")
    
    ipca_api_months = get_ipca_last_months(months) # requisição do awesomeapi

    # 🟡 tratando os dados

    # ◻️ preço do ipca
    ipca_prices = []
    for ipca in ipca_api_months:
        price = convert_float(ipca['valor'])
        ipca_prices.append(price)

    # ◻️ datas
    months_week = get_months(months)
    

    CONTEXT = {
        'ipca_prices': ipca_prices,
        'months_week': months_week
    }

    return JsonResponse(CONTEXT)

def get_inpc_for_months(request: HttpRequest, months: int=5):
    '''
    Função de api para enviar ao frontend a media do inpc
    em um intervalo de meses

    parâmetros:
        months = numero de meses para pegar a media

    retorna:
        json com as medias do inpc
    '''

    # Valida os parâmetros
    # tambem inpõe um limite de 1 mês
    if not isinstance(months, int) or months >= 30:
        raise Http404("O parâmetro 'months' deve ser um inteiro maior que 0 e menor que 31.")
    
    inpc_api_price_months = get_inpc_last_months(months) # requisição do awesomeapi

    # 🟡 tratando os dados

    # ◻️ preço do inpc
    inpc_prices = []
    for inpc in inpc_api_price_months:
        price = convert_float(inpc['valor'])
        inpc_prices.append(price)
    

    CONTEXT = {
        'inpc_prices': inpc_prices,
    }

    return JsonResponse(CONTEXT)

def get_selic_for_months(request: HttpRequest, months: int=5):
    '''
    Função de api para enviar ao frontend a media do selic
    em um intervalo de meses

    parâmetros:
        months = numero de meses para pegar a media

    retorna:
        json com as medias do selic
    '''

    # Valida os parâmetros
    # tambem inpõe um limite de 1 mês
    if not isinstance(months, int) or months >= 30:
        raise Http404("O parâmetro 'months' deve ser um inteiro maior que 0 e menor que 31.")
    

    # 🟡 tratando os dados
    # ◻️ preço do selic
    selic_prices = get_selic_last_months(months) # requisição do gov
    
    # ◻️ datas
    months_week = get_months(months)
    

    CONTEXT = {
        'selic_prices': selic_prices,
        'months_week': months_week
    }

    return JsonResponse(CONTEXT)


    




    

