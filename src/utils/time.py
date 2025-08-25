from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 

def get_days_week(qtd_dias: int = 1) -> list[str]:
    """
    Retorna os dias da semana para os últimos 'qtd_dias' dias, incluindo hoje.

    🔴 PARAMETROS 🔴
    qtd_dias: quantidade de dias a retornar (inclui o dia de hoje).
    
    Retorno:
    Lista com os nomes dos dias da semana em português.
    """


    # Lista com nomes dos dias da semana (começando em segunda)
    dias_semana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]

    hoje = datetime.now()
    resultado = []

    for i in range(qtd_dias):
        data = hoje - timedelta(days=i) # i começa por 0 caso haja duvidas
        indice = data.weekday()  # Retorna 0 para segunda, 6 para domingo
        resultado.append(dias_semana[indice])

    return resultado


def get_months(qtd_meses: int = 1) -> list[str]:
    """
    Retorna os meses para os últimos 'qtd_meses' meses, incluindo o mês atual.

    🔴 PARAMETROS 🔴
    qtd_meses: quantidade de meses a retornar (inclui o mês atual).
    
    Retorno:
    Lista com os nomes dos meses em português abreviados.
    """
    
    # Lista com nomes dos meses
    meses_ano = ["jan", "fev", "mar", "abr", "mai", "jun", 
                 "jul", "ago", "set", "out", "nov", "dez"]

    hoje = datetime.now()
    resultado = []

    for i in range(qtd_meses):
        data = hoje - relativedelta(months=i) # i começa por 0
        indice = data.month - 1  # month retorna 1 a 12
        resultado.append(meses_ano[indice])

    return resultado


def get_today():
    """
    Retorna a data atual no formato 'dia/mês/ano'.
    """
    hoje = datetime.now()  # pega a data e hora atual
    return hoje.strftime("%d/%m/%Y")  # formata só a data

def removed_months(data_str: str, months: int=1) -> str:
    """
    Remove 'days' dias da data 'data_str'.

    parametros:
        data_str = string com a data no formato 'dia/mês/ano'
        days = quantidade de dias a serem removidos

    retorna:
        string com a nova data
    """
    # Converte string para datetime
    data = datetime.strptime(data_str, "%d/%m/%Y")
    # Subtrai 1 mês
    nova_data = data - relativedelta(months=months)
    # Retorna como string
    return nova_data.strftime("%d/%m/%Y")




if __name__ == "__main__":
    print(get_days_week(2))
    print(get_months(2))
    print(get_today())
    print(removed_months("2023/01/01"))
