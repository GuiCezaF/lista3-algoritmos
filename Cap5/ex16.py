'''
Considere a lista

planetas = ['Mercúrio', 'Vênus', 'Terra', Marte', 'Saturno', 'Júpiter', 'Urano', 'Netuno'].

Execute as seguintes operações usando apenas fatiamento. Cada item usa a lista resultante do item anterior.

1.Insira a lista ['Fobos','Deimos'] na posição 4 da lista.

2.Insira ['Sol'] na posição zero.

3.Qual seria o fatiamento para imprimir ['Urano', 'Júpiter', 'Saturno', 'Deimos', 'Fobos', 'Marte', 'Terra', 'Vênus'], nessa ordem?
'''
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte',
            'Saturno', 'Júpiter', 'Urano', 'Netuno']

planetas[4:4] = ['Fobos', 'Deimos']
print(planetas)

planetas[:0] = ['Sol']
print(planetas)

resultado = planetas[6:0:-1] + planetas[4:6] + planetas[3:1:-1] + planetas[0:1]
print(resultado)
