'''
Reescreva o Programa 5.13 usando o comando while.
'''

print('Tabela de conversão de Fahrenheit para Celsius')

fahr = 0

while fahr <= 300:
    celsius = (5/9)*(fahr - 32)
    print('{:>5d} -> {:>5.1f}'.format(fahr, celsius))
    fahr += 20
