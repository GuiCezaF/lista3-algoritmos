'''
Escreva um programa para gerar uma lista com o quadrado dos números pares entre 10 e 20 (inclusive).
'''


def lista_quadrados_pares() -> int:
    quadrados_pares = []
    for numero in range(10, 21):
        if numero % 2 == 0:
            quadrado = numero ** 2
            quadrados_pares.append(quadrado)
    return quadrados_pares

print(lista_quadrados_pares())