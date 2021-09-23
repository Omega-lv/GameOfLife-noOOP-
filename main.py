from random import *
seed(1)
print("Juego de la vida")
print("\n")
columnas= int(input("Introduce numero de columnas: "))
print("\n")
filas= int(input("Introduce numero de filas: "))
contadorFilas=0
contadorColumnas=0
while contadorFilas<filas:
    contadorColumnas=0
    while contadorColumnas<columnas:
        aleatorio=random()
        if aleatorio>0.55:
            print(0, end='')
        else:
            print("-", end='')
        contadorColumnas=contadorColumnas+1
        print(" ", end='')
    print("\n")
    contadorFilas=contadorFilas+1
usuario=input("Introduzca 'n' para ver la siguiente generación o 'q' para finalizar el programa")
if usuario=="q":
    exit()

#toca ahora ver como calculamos la siguiente generacion
#quiza definir un metodo que lo calcule sea lo más cómodo
#leete las reglas del juego tamien