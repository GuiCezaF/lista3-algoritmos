'''
Escreva um programa que dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gere a lista [1, 3, 5, 7, 9, 0, 2, 4, 6, 8].
'''

lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_desejada = []

for elemento in lista_original:
    if elemento % 2 == 1:
        lista_desejada.append(elemento)

for elemento in lista_original:
    if elemento % 2 == 0:
        lista_desejada.append(elemento)

print(lista_desejada)
