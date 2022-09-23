from logging import raiseExceptions


x = int(input("Introduzca número de filas: "))
y = int(input("Introduzca número de columnas: "))

if x <1 or x>9:
    raise Exception("El número x tiene que estar contenido entre 1 y 9")

if y <1 or y>9:
    raise Exception("El número y tiene que estar contenido entre 1 y 9")


for x1 in range(x):
    print("")
    for y1 in range(y):
        print("*", end='')