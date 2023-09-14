'''
Modifique o Programa 4.16 de modo que a função que gera coordenadas aleatórias
receba como parâmetro o número de coordenadas que precisam ser geradas e devolva
uma lista de tuplas com essas coordenadas.
Deste modo, a função que calcula o valor de pi também precisa ser modificada 
para tratar essas coordenadas em forma de lista de tuplas.
'''

import random as r
import math as m


def gera_coordenadas_aleatorias(n):
    '''Gera uma lista de n pares de coordenadas aleatórias.'''

    coordenadas = [(r.random(), r.random()) for _ in range(n)]

    return tuple(coordenadas)


def coordenadas_dentro_circulo(x, y):
    '''Testa se coordenadas estão dentro do círculo de raio 1.'''

    return m.hypot(x, y) < 1


def calcula_pi(coordenadas):
    '''Calcula pi e o erro associado a partir de uma lista de coordenadas.'''

    conta_circulo = 0

    for x, y in coordenadas:
        if coordenadas_dentro_circulo(x, y):
            conta_circulo += 1

    pi = 4 * conta_circulo / len(coordenadas)
    erro = m.fabs(pi - m.pi)

    return pi, erro


num = int(input('Quantos pontos devem ser sorteados? '))

coordenadas = gera_coordenadas_aleatorias(num)
pi, erro = calcula_pi(coordenadas)

print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)
