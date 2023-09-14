'''
O que acontece se o terceiro parâmetro de uma operação de fatiamento for -1?
Teste em uma lista qualquer o comando lista[::-1].
Qual a diferença para reverse()?
'''

minha_lista = [1, 2, 3, 4, 5]
reverso = minha_lista[::-1]
print(reverso)

minha_lista.reverse()
print(minha_lista)


# A principal diferença entre usar o fatiamento [:: -1] e o método reverse()
# é que o fatiamento [:: -1] cria uma nova lista invertida sem modificar a lista original,
# enquanto o método reverse() inverte a ordem dos elementos na própria lista original.
