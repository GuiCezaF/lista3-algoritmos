'''
Escreva um programa que dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gere a lista [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
'''

lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n_elementos = 5

lista_desejada = lista_original[n_elementos:] + lista_original[:n_elementos]

print(lista_desejada)
