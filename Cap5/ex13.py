'''
Dada a lista [10, 2, 32, 14, 35, 46, 17, 58, 199, 19], escreva um programa que imprima:

1.os elementos de índices pares;

2.os elementos de índices ímpares;

3.os elementos entre os índices 2 (inclusive) e 4 (exclusive);

4.o elemento de índice 1 e depois os elementos distantes 3 posições a partir de 1, até o final.
'''

lista = [10, 2, 32, 14, 35, 46, 17, 58, 199, 19]

print("Elementos de índices pares:")
for i in range(0, len(lista), 2):
    print(lista[i])

print("\nElementos de índices ímpares:")
for i in range(1, len(lista), 2):
    print(lista[i])

print("\nElementos entre os índices 2 e 4:")
for i in range(2, 4):
    print(lista[i])

print("\nElemento de índice 1 e elementos distantes 3 posições a partir de 1:")
print(lista[1])
for i in range(4, len(lista), 3):
    print(lista[i])
