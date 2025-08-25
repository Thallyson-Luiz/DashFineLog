def convert_float(value) -> float:
    '''
    parametros:
        value = valor a ser convertido
    retorna:
        valor convertido para float ou 0 caso nao seja possivel
    '''

    try:
        value = float(value)
    except:
        value = 0

    return value