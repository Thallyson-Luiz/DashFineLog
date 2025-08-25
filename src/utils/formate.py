def formatar_numero(numero: float) -> str:
    """
    Formata um número grande com pontos como separador de milhar e duas casas decimais
    
    🔴 PARAMETROS 🔴
    numero: O número (inteiro ou float) a ser formatado
    
    Retorna:
    Uma string com o número formatado, usando ponto como separador de milhar
    e mantendo até duas casas decimais se for um float
    """
    # Verifica se é inteiro ou decimal
    if isinstance(numero, int) or numero.is_integer():
        # Número inteiro: formata apenas com pontos
        return f"{int(numero):,}".replace(",", ".")
    else:
        # Número decimal: formata com pontos nos milhares e vírgula para decimal
        inteiro, decimal = f"{numero:,.2f}".split(".")
        inteiro_formatado = inteiro.replace(",", ".")
        return f"{inteiro_formatado},{decimal}"



if __name__ == "__main__":
    print(formatar_numero(1234567.89))
    print(formatar_numero(1234567))
    print(formatar_numero(1234.56))
