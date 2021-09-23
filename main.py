from random import *

"""
import numpy as np
"""

#FUNCION ENCARGADA DE IMPRIMRIR POR PANTALLA EL MAPA CON CELULAS VIVAS Y MUERTAS
#SE LE PASA COMO PARAMETRO UNA MATRIZ
def plotea_mapas(mapa):
    contadorFilas=0
    contadorColumnas=0
    while contadorFilas<filas:
        contadorColumnas=0
        while contadorColumnas<columnas:
            print(mapa[contadorFilas][contadorColumnas], end='')
            contadorColumnas=contadorColumnas+1
            print(" ", end='')
        print("\n")
        contadorFilas=contadorFilas+1




seed(1)
print("Juego de la vida")
print("\n")
"""
#DE MOMENTO UTILIZAREMOS UNO GENERADO A PELO
#MÁS ADELANTE BUSCAREMOS LA FORMA DE HACERLO GENERICO
columnas= int(input("Introduce numero de columnas: "))
print("\n")
filas= int(input("Introduce numero de filas: "))
"""
contadorFilas=0
contadorColumnas=0


#CREACION DEL MAPA INICIAL
#DE MOMENTO UTILIZAREMOS UNO GENERADO A PELO
#MÁS ADELANTE BUSCAREMOS LA FORMA DE HACERLO GENERICO
mapa = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#lineas de chapuceo aqui mientras trabajamos
#QUITAR CUANDO QUERAMOS QUE EL INPUT DEL USUARIO VALGA DE ALGO
columnas=8
filas=6
plotea_mapas(mapa)
while contadorFilas<filas:
    contadorColumnas=0
    while contadorColumnas<columnas:
        aleatorio=random()
        if aleatorio<0.55:
            mapa[contadorFilas][contadorColumnas]=0
        else:
            mapa[contadorFilas][contadorColumnas]=1
        contadorColumnas=contadorColumnas+1
    contadorFilas=contadorFilas+1

#PINTAMOS EL MAPA INICIAL
print("El mapa inicial")
plotea_mapas(mapa)

"""
#PASO A LA SIGUIENTE RONDA
usuario=input("Introduzca 'n' para ver la siguiente generación o 'q' para finalizar el programa")
if usuario=="q":
exit()

#toca ahora ver como calculamos la siguiente generacion
#quiza definir un metodo que lo calcule sea lo más cómodo
#leete las reglas del juego tamien


PROBABILIDADES NO PARECEN FUNCIONAR CORRECTAMENTE

"""