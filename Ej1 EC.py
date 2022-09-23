




matriz = [

    [1, 1, 1, 3],

    [2, 2, 2, 7],

    [3, 3, 3, 9],

    [4, 4, 4, 13]

]

print(matriz)

for x in range(len(matriz)):
    f=0
    for y in range(len(matriz[x])):
        if y == (len(matriz[x])-1):
            matriz[x][y]=f
        else:
            f+= int(matriz[x][y])


print(matriz)