import requests
from utils.calc_variation import calc_variation_percent



def get_coins_today(tickers_pars: list[str]) -> list[dict]:
    '''
    Função para extrair a cotação de varias moedas no dia de hoje pelo AwesomeAPI.

    parâmetros:
        ticlers_pars = list com as siglas das moedas e o par de negociação
    retorna:
        list[dict] com as cotações das moedas
    
    Exemplo:
        get_coins_today(["BTC-BRL", "ETH-BRL"])
    '''

    # URL para obter os dados do AwesomeAPI
    url = f"https://economia.awesomeapi.com.br/json/last/"

    # Adiciona o par de negociação aos tickers
    for i, ticker in enumerate(tickers_pars):

        if i == len(tickers_pars) - 1:
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
        return [JSON_RESONSE[f"{ticker.replace('-', '')}"] for ticker in tickers_pars]
    except :
        return list() # Em caso de erro, retorna um dicionário vazio
    
def get_coin_today(ticker: str, trading_pair: str) -> dict:
    """
    Função para extrair a cotação de uma moeda no dia de hoje pelo AwesomeAPI.

    Parâmetros:
        ticker (str): Sigla da moeda.
        trading_pair (str): Par de negociação da moeda.
    
    Retorna:
        dict com a cotação da moeda hoje.

    Exemplo:
        get_coin_today("BTC", "BRL")

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



def config_coin_today(coins) -> list[dict]:
    """
    Função para configurar os dados das moedas para o template my_coins.

    Parâmetros:
        criptos (QuerySet): QuerySet com os dados das moedas.

    Retorna:
        list[dict]: Lista com os dados das moedas.

    Exemplo:
        config_coin_today(coins)
    """

    # variaveis para obter os dados
    list_coins = []

    # adicionando os tickers ao list
    for coin in coins:
        list_coins.append(f"{coin.ticker}-{coin.trading_pair}")

        


    # obtendo os dados brutos
    COINS_RAW_DATA = get_coins_today(list_coins)

    if not COINS_RAW_DATA:
        return list()
    

    # tratando os dados
    coins_info = []
    for i, coin in enumerate(COINS_RAW_DATA):

        dict_result = dict() # cria um dicionario para armazenar os dados da moedas
        NAME_COIN = f"{coin['code']}/{coin['codein']}" # nome da moedas

        # calculo da variacao
        COIN_NOW = float(coin['bid'])
        COIN_BEFORE = COIN_NOW + float(coin['varBid'])
        COIN_PERCENTAGE = calc_variation_percent(COIN_BEFORE, COIN_NOW)


        
        # adiciona os dados ao dicionario
        dict_result['name'] = NAME_COIN # adiciona o nome da moedas ao dicionario
        dict_result['price'] = coin['bid'] # adiciona a cotação da moedas ao dicionario
        dict_result['variation'] = COIN_PERCENTAGE # adiciona a variacao da moedas ao dicionario
        coins_info.append(dict_result) # adiciona o dicionario a lista


    return coins_info