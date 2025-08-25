import requests


def get_pib_last_months(n_months: int) -> list[dict]:
    """
    Retorna os valores do PIB dos últimos n meses.

    Parâmetros:
        n_months (int): número de meses anteriores para buscar os dados

    Retorna:
        list: lista de dicionários com mês e valor do PIB
              ex: [{'mes': '2025-08', 'valor': 0.32}, ...]

    Atenção:
        O número de meses deve estar entre 1 e 12
    """
    # Tratando número de meses
    if not isinstance(n_months, int) or n_months < 1 or n_months > 12:
        raise ValueError("O parâmetro 'n_months' deve ser um inteiro maior que 0 e menor que 13.")

    # Buscando os dados do PIB (código 24364 no SGS)
    URL = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.24364/dados/ultimos/{n_months}?formato=json"

    # Fazendo a requisição
    response = requests.get(URL)

    # Verificando se houve erro na requisição
    if response.status_code != 200:
        return list()

    # Retornando os dados em JSON
    return response.json()



# exemplos de uso

if __name__ == "__main__":
    print(get_pib_last_months(6))