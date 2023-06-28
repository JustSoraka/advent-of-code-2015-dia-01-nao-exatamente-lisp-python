ACOES_INSTRUCAO = {
    "(": 1,  # Incrementa o andar em 1
    ")": -1  # Decrementa o andar em 1
}


def calcular_andar(instrucoes):
    """
    Calcula o andar final com base nas instruções dadas.
    Uma abertura de parêntese '(' indica subida de um andar.
    Um fechamento de parêntese ')' indica descida de um andar.
    """
    andar_atual = 0
    for instrucao in instrucoes:
        andar_atual += ACOES_INSTRUCAO.get(instrucao, 0)
    return andar_atual


def imprimir_resultado(instrucoes, andar_final):
    print(f"Instruções: {instrucoes}")
    print(f"Andar resultante: {andar_final}")
    print()


# Lista de instruções
lista_instrucoes = [
    "(())",
    "()()",
    "((((",
    "(()(()(",
    "))(((((",
    "())",
    "))(",
    ")))",
    ")())())"
]

# Imprimir os resultados diretamente em um loop
for instrucoes in lista_instrucoes:
    andar_final = calcular_andar(instrucoes)
    imprimir_resultado(instrucoes, andar_final)