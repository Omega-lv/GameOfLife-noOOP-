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


#FUNCION ENCARGADA DE ANALIZAR SITUACION ALREDEDOR DE LA CELULA Y SUMAR CUANTOS VIVOS HAY
def cuantosVivientes (mapa, contadorFilas, contadorColumnas):
    contadorinVivos=0
    if contadorFilas==0:
        if contadorColumnas==0:
            if mapa[contadorFilas][contadorColumnas+1]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas+1]==1:
                contadorinVivos=contadorinVivos+1
        if contadorColumnas==columnas-1:
            if mapa[contadorFilas][contadorColumnas-1]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas-1]==1:
                contadorinVivos=contadorinVivos+1
        else:
            if mapa[contadorFilas][contadorColumnas-1]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas][contadorColumnas+1]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas-1]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas]==1:
                contadorinVivos=contadorinVivos+1
            if mapa[contadorFilas+1][contadorColumnas+1]==1:
                contadorinVivos=contadorinVivos+1
    else:
        if contadorFilas==filas-1:
            if contadorColumnas==0:
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
            if contadorColumnas==columnas-1:
                if mapa[contadorFilas][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
            else:
                if mapa[contadorFilas][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
        else:
            if contadorColumnas==0:
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
            if contadorColumnas==columnas-1:
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
            else:
                if mapa[contadorFilas-1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas-1]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas+1][contadorColumnas]==1:
                    contadorinVivos=contadorinVivos+1
                if mapa[contadorFilas-1][contadorColumnas+1]==1:
                    contadorinVivos=contadorinVivos+1
    return contadorinVivos







    


#FUNCION ENCARGADA DE ANALIZAR LA SITUACION DE LAS CELULAS VIVAS Y MODIFICAR SU ESTADO SU FUESE NECESARIO
def analisis_celula_viva (mapa, mapa_apoyo, contadorFilas, contadorColumnas):
    contadorVivos=0
    contadorVivos=cuantosVivientes(mapa,contadorFilas,contadorColumnas)
    if contadorVivos==2 or contadorVivos==3:
        mapa_apoyo[contadorFilas][contadorColumnas]=1
    else:
        mapa_apoyo[contadorFilas][contadorColumnas]=0

#FUNCION ENCARGADA DE ANALIZAR LA SITUACION DE LAS CELULAS MUERTAS Y MODIFICAR SU ESTADO SU FUESE NECESARIO
def analisis_celula_muerta (mapa, mapa_apoyo, contadorFilas, contadorColumnas):
    contadorVivos=0
    contadorVivos=cuantosVivientes(mapa,contadorFilas,contadorColumnas)
    if contadorVivos==3:
        mapa_apoyo[contadorFilas][contadorColumnas]=1
    else:
        mapa_apoyo[contadorFilas][contadorColumnas]=0

def pasador(mapa, mapa_apoyo, filas, columnas):
    contadorceteFilas=0
    contadorceteColumnas=0
    while contadorceteFilas<filas:
        contadorceteColumnas=0
        while contadorceteColumnas<columnas:
            mapa[contadorceteFilas][contadorceteColumnas]=mapa_apoyo[contadorceteFilas][contadorceteColumnas]
            contadorceteColumnas=contadorceteColumnas+1
        contadorceteFilas=contadorceteFilas+1


seed(1)
print("Juego de la vida")
print("\n")
"""
columnas= int(input("Introduce numero de columnas: "))
print("\n")
filas= int(input("Introduce numero de filas: "))
"""
contadorFilas=0
contadorColumnas=0


#CREACION DEL MAPA INICIAL
#DE MOMENTO UTILIZAREMOS UNO GENERADO A PELO
#MÁS ADELANTE BUSCAREMOS LA FORMA DE HACERLO GENERICO
mapa = [[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0]]
mapa_apoyo = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#lineas de chapuceo aqui mientras trabajamos
#QUITAR CUANDO QUERAMOS QUE EL INPUT DEL USUARIO VALGA DE ALGO
columnas=8
filas=3




plotea_mapas(mapa)

"""
#GENERAMOS MAPA INICIAL
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
"""

#PINTAMOS EL MAPA INICIAL
print("El mapa inicial")
plotea_mapas(mapa)


#PASO A LA SIGUIENTE RONDA
usuario=input("Introduzca 'n' para ver la siguiente generación o 'q' para finalizar el programa: ")
if usuario=="q":
    exit()

#toca ahora ver como calculamos la siguiente generacion
#quiza definir un metodo que lo calcule sea lo más cómodo
#leete las reglas del juego tamien

contadorFilas=0
contadorColumnas=0
while contadorFilas<filas:
    contadorColumnas=0
    while contadorColumnas<columnas:
        if mapa[contadorFilas][contadorColumnas]==1:
            analisis_celula_viva(mapa,mapa_apoyo,contadorFilas,contadorColumnas)
        else: 
            analisis_celula_muerta(mapa,mapa_apoyo,contadorFilas,contadorColumnas)
        contadorColumnas=contadorColumnas+1
    contadorFilas=contadorFilas+1


#PASAMOS DATOS DE EL MAPA DE APOYO AL MAPA BASE
pasador(mapa, mapa_apoyo, filas, columnas)

plotea_mapas(mapa)



"""
NECESITAMOS ARREGLAR LA CREACION DEL MAPA
(funciona pero todo es dependiente de array_apoyo ahora)

#PRUEBA DE SISTEMA DE CREACION DE MAPA INICIAL
mapa=[0]*columnas
contador_inicial=0
array_apoyo=[0]*columnas
mapa=[mapa]+[array_apoyo]
while contador_inicial<filas-2:
    mapa=mapa+[array_apoyo]
    contador_inicial=contador_inicial+1


POSIBILIDAD, HACER UNA FUNCION QUE SE LLAME CONTADOR DE VIVOS O ALGO ASI QUE AGLUTINE LOS IFS CONJUNTOS QUE TENEMOS REPETIDOS DOS VECES
PA VER SI SANEAMOS UN POCO ESE CACHO DE CODIGO

"""