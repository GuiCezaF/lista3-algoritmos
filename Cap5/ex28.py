'''
Escreva um programa que crie uma matriz tridimensional
usando o mecanismo de lista por compreensão.
'''
dim_x = 3
dim_y = 3
dim_z = 3

matriz_3d = [[[0 for _ in range(dim_z)] for _ in range(dim_y)] for _ in range(dim_x)]

for x in range(dim_x):
    for y in range(dim_y):
        for z in range(dim_z):
            print(f"matriz_3d[{x}][{y}][{z}] = {matriz_3d[x][y][z]}")


