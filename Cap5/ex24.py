'''
Partindo da lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
use os comandos desta seção para obter [5, 6, 7, 8, 9, 4, 3, 2, 1, 0].
'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeira_metade_invertida = lista[:5][::-1]
segunda_metade = lista[5:]
lista = segunda_metade + primeira_metade_invertida

print(lista)
