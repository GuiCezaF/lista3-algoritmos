'''
Os dicionários de Python não são ordenados,
pois sua função principal é a busca rápida de uma informação baseada em uma chave.
Modifique o programa sobre aeroportos desta seção para trabalhar apenas com tuplas,
eliminando o dicionário e usando o nome da cidade como primeiro elemento da tupla.
'''
lat_galeao = (22, 48, 34)
long_galeao = (43, 15, 0)
aeroporto_galeao = ('Galeão', lat_galeao, long_galeao)

lat_guarulhos = (23, 26, 6)
long_guarulhos = (46, 28, 22)
aeroporto_guarulhos = ('Guarulhos', lat_guarulhos, long_guarulhos)

aeroportos = [
    aeroporto_galeao,
    aeroporto_guarulhos
]

for aeroporto in aeroportos:
    cidade = aeroporto[0]
    latitude = f'{aeroporto[1][0]}º{aeroporto[1][1]}"{aeroporto[1][2]}"'
    longitude = f'{aeroporto[2][0]}º{aeroporto[2][1]}"{aeroporto[2][2]}"'

    print(
        f'Aeroporto {cidade}:\n\t{aeroporto[0]}\n\tLatitude: {latitude}\n\tLongitude: {longitude}')
