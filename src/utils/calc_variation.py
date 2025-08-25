def calc_variation_percent(value_one: float, value_two: float) -> float:
    '''
    parametros:
        value_one = valor 1
        value_two = valor 2
    retorna:
        variacao percentual
    '''
    return round((value_two - value_one) / value_one * 100, 2)


if __name__ == "__main__":
    print(calc_variation_percent(1, 1.0001))
    