'''
Crie uma lista com os números ímpares entre 0 e 100
(use range()) e depois use o comando enumerate()
para percorrer a lista transformando o valor de cada elemento no valor par subsequente.
'''

numeros_impares = list(range(1, 101, 2))


for indice, valor in enumerate(numeros_impares):
    numeros_impares[indice] = valor + 1

print(numeros_impares)
