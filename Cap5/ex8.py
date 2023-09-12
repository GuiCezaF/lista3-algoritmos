'''
Escreva um programa para gerar uma lista com o quadrado dos números ímpares de 0 a 9, como no Programa 5.16,
porém não use filtros. Use apenas o comando range() para controlar a geração da sequência de números ímpares.
'''

quadrados_impares = []

for numero in range(10):
    if numero % 2 == 1:
        quadrado = numero ** 2
        quadrados_impares.append(quadrado)

print(quadrados_impares)
