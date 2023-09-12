'''
Escreva um programa que crie uma lista com o cubo dos números entre 1 e 10, ambos inclusive.
'''


def lista_cubos() -> int:
    lista_cubos = []
    for numero in range(0, 11):
        cubo = numero ** 3
        lista_cubos.append(cubo)
    return lista_cubos
  
print(lista_cubos())