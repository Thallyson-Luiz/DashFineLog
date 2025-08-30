def calc_variation_percent(value_start: float, value_end: float) -> float:
    '''
    calcula a variacao percentual entre dois valores
    
    parametros:
        value_start = preco inicial
        value_end = preco final

    ex:
        value_start = 5
        value_end = 3.1

    retorna:
        variacao percentual
    '''
    return round((value_end - value_start) / value_start * 100, 2)


if __name__ == "__main__":
    print(calc_variation_percent(5, 3.1))
    