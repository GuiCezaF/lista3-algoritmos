'''
Use os comandos desta seção para inverter os elementos da primeira metade de uma lista.
Por exemplo, se a lista é lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
use os comandos para obter [4, 3, 2, 1, 0, 5, 6, 7, 8, 9].
'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

primeira_metade_invertida = lista[:len(lista)//2][::-1]

lista = primeira_metade_invertida + lista[len(lista)//2:]

print(lista)
