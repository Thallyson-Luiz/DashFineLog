import requests
from utils.calc_variation import calc_variation_percent

def get_dolar_today() -> dict:
    """
    função para extrair a cotação do dólar em relação ao real no dia de hoje pelo awesomeapi.
    
    Retorna:
    dict com a cotação do dólar hoje.
    """

    # Url para obter os dados do awesomeapi
    URL = f"https://economia.awesomeapi.com.br/json/last/USD-BRL"

    # Faz a requisição 
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return dict()
    
    # Retorna o resultado em JSON
    response = response.json()

    # Retorna os campos da cotação
    return response['USDBRL']



def get_dolar_with_days(days: int=6) -> list[dict]:
    '''
    parâmetros:
        days = numero de dias para pega a cotação
    retorna:
        list[dict] com as cotações de dias especificados
    '''

    # Url para obter os dados do banco central
    URL = f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{days}"


    # Faz a requisição
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return list()

    # Retorna os dados em JSON
    return response.json()

def calc_coin_variation(price: float, price_variation: float) -> float:
    '''
    parametros:
        price = preco atual
        price_variation = preco da variacao ex: 0.01 dolar
    retorna:
        variacao percentual
    '''
    
    COIN_BEFORE = price - price_variation
    COIN_PERCENTAGE = calc_variation_percent(COIN_BEFORE, price)

    return COIN_PERCENTAGE




if __name__ == "__main__":
    # print(get_dolar_today())
    print(get_dolar_with_days())
    # print(calc_dolar_variation(1, 0.01))