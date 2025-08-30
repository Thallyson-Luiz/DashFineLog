import requests
from utils.calc_variation import calc_variation_percent

def get_bitcoin_today() -> dict:
    """
    Função para extrair a cotação do Bitcoin em relação ao real no dia de hoje pelo AwesomeAPI.
    
    Retorna:
    dict com a cotação do Bitcoin hoje.
    """

    # URL para obter os dados do AwesomeAPI
    URL = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"

    # Faz a requisição
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return dict()
    
    # Retorna o resultado em JSON
    response = response.json()

    # Retorna os campos da cotação
    return response['BTCBRL']



def get_bitcoin_with_days(days: int = 6) -> list[dict]:
    '''
    parâmetros:
        days = número de dias para pegar a cotação do Bitcoin em relação ao Real
    retorna:
        list[dict] com as cotações de dias especificados
    '''

    # URL para obter os dados do AwesomeAPI
    URL = f"https://economia.awesomeapi.com.br/json/daily/BTC-BRL/{days}"

    # Faz a requisição
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return list()

    # Retorna os dados em JSON
    return response.json()

def get_cripto_today(ticker: str, trading_pair: str) -> dict:
    """
    Função para extrair a cotação de uma criptomoedano dia de hoje pelo AwesomeAPI.

    Parâmetros:
        ticker (str): Sigla da criptomoeda.
        trading_pair (str): Par de negociação da criptomoeda.
    
    Retorna:
        dict com a cotação da criptomoeda hoje.

    Exemplo:
        get_cripto_today("BTC", "BRL")

    Em caso de erro, retorna um dicionário vazio.
    """

    # URL para obter os dados do AwesomeAPI
    try:
        URL = f"https://economia.awesomeapi.com.br/json/last/{ticker}-{trading_pair}"
    except:
        return dict()

    # Faz a requisição
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return dict()
    
    # Retorna o resultado em JSON
    response = response.json()

    # Retorna os campos da cotação
    try:
        return response[f'{ticker}{trading_pair}']
    except:
        return dict() # Em caso de erro, retorna um dicionário vazio
    


def get_criptos_today(tickers: list[str], trading_pair: str) -> list[dict]:
    '''
    Função para extrair a cotação de varias criptomoedas no dia de hoje pelo AwesomeAPI.

    parâmetros:
        tickers = list com as siglas das criptomoedas
        trading_pair = par de negociação das criptomoedas
    retorna:
        list[dict] com as cotações das criptomoedas
    
    Exemplo:
        get_criptos_today(["BTC", "ETH"], "BRL")
    '''

    # URL para obter os dados do AwesomeAPI
    url = f"https://economia.awesomeapi.com.br/json/last/"

    # Adiciona o par de negociação aos tickers
    for i, ticker in enumerate(tickers):
        ticker = f"{ticker}-{trading_pair}"

        if i == len(tickers) - 1:
            url = f"{url}{ticker}"
            break

        url = f"{url}{ticker},"

    

    # Faz e testa a requisição
    try:
        RESPONSE = requests.get(url)
    except:
        return list()
    

    # Verifica se houve erro na requisição
    if RESPONSE.status_code != 200:
        return list()
    
    # Caso de certo, retorna o resultado em JSON
    JSON_RESONSE = RESPONSE.json()

    # Retorna os campos da cotação
    try:
        return [JSON_RESONSE[f"{ticker}{trading_pair}"] for ticker in tickers]
    except:
        return list() # Em caso de erro, retorna um dicionário vazio
    

    
def config_cripto_today(criptos) -> list[dict]:
    """
    Função para configurar os dados das criptomoedas para o template cripto.

    Parâmetros:
        criptos (QuerySet): QuerySet com os dados das criptomoedas.

    Retorna:
        list[dict]: Lista com os dados das criptomoedas.

    Exemplo:
        config_cripto_today(criptos)
    """

    # variaveis para obter os dados
    list_criptos = []
    url_image_list = []
    TRADING_PAIR = criptos.first().trading_pair

    # adicionando os tickers ao list
    for cripto in criptos:
        list_criptos.append(cripto.ticker)
        url_image_list.append(cripto.img.url)
        


    # obtendo os dados brutos
    CRIPTO_RAW_DATA = get_criptos_today(list_criptos, TRADING_PAIR)

    if not CRIPTO_RAW_DATA:
        raise Exception("Erro ao obter os dados das criptomoedas")
    



    # tratando os dados
    criptos_info = []
    for i, cripto in enumerate(CRIPTO_RAW_DATA):

        dict_result = dict() # cria um dicionario para armazenar os dados da criptomoeda
        NAME_COIN = f"{cripto['code']}/{cripto['codein']}" # nome da criptomoeda

        # calculo da variacao
        COIN_NOW = float(cripto['bid'])
        COIN_BEFORE = COIN_NOW + float(cripto['varBid'])
        COIN_PERCENTAGE = calc_variation_percent(COIN_BEFORE, COIN_NOW)


        
        # adiciona os dados ao dicionario
        dict_result['name'] = NAME_COIN # adiciona o nome da criptomoeda ao dicionario
        dict_result['price'] = cripto['bid'] # adiciona a cotação da criptomoeda ao dicionario
        dict_result['variation'] = COIN_PERCENTAGE # adiciona a variacao da criptomoeda ao dicionario
        dict_result['img'] = url_image_list[i] # adiciona a imagem da criptomoeda ao dicionario
        criptos_info.append(dict_result) # adiciona o dicionario a lista


    return criptos_info

def get_market_humor() -> dict:
    """
    Função para extrair o humor do mercado pelo AlternativeAPI.

    Retorna:
        dict com o humor do mercado.

    Exemplo:
        get_market_humor()
    """

    # Url para obter os dados
    URL = "https://api.alternative.me/fng/"

    # Faz a requisição
    response = requests.get(URL)

    # Verifica se houve erro na requisição
    if response.status_code != 200:
        return dict()
    
    # Retorna o resultado em JSON
    try:
        return response.json()['data'][0]
    except:
        return dict()





if __name__ == "__main__":
    # print(get_bitcoin_today())
    # print(get_bitcoin_with_days(1))
    # print(get_criptos_today(["BTC", "ETH", "LTC"], "BRL"))
    print(get_market_humor())
