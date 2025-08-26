import requests

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



if __name__ == "__main__":
    print(get_bitcoin_today())
    print(get_bitcoin_with_days(1))