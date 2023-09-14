'''
Escreva um programa que inverta uma lista usando o método de lista por compreensão.
'''

minha_lista = [1, 2, 3, 4, 5]
inverso = [minha_lista[i] for i in range(len(minha_lista) - 1, -1, -1)]
print(inverso)
