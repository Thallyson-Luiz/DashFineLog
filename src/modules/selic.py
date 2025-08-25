import requests
from utils.time import get_today, removed_months
def get_selic_last_months(n_months: int) -> list[dict]:
    """
    Retorna os valores da taxa Selic dos últimos n meses.

    Parâmetros:
        n_months (int): número de meses anteriores para buscar os dados

    Retorna:
        list: lista de dicionários com mês e valor da Selic
              ex: [{'mes': '2025-08', 'valor': 0.0551}, ...]

    Atenção:
        O número de meses deve estar entre 1 e 12
    """
    # Tratando número de meses
    if not isinstance(n_months, int) or n_months < 1 or n_months > 12:
        raise ValueError("O parâmetro 'n_months' deve ser um inteiro maior que 0 e menor que 13.")
    
    today = get_today()  # pega a data atual
    before_day = removed_months(today, (n_months - 1))  # pega a data antes de n meses

    # Buscando os dados da Selic mensal (código 432 no SGS)
    URL = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json&dataInicial={before_day}&dataFinal={today}"

    # Fazendo a requisição
    response = requests.get(URL)

    # Verificando se houve erro na requisição
    if response.status_code != 200:
        return list()

    # Retornando os dados em JSON
    dados = response.json()
    return [dado["valor"] for dado in dados]



if __name__ == "__main__":
    print(get_selic_last_months(11))
