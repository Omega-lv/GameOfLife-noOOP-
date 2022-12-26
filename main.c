#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void printea_matriz(int** matriz, int size){

    int i;
    int j;
    printf("\n");
    for (i=0; i<size; i++){
        printf("|");
        for (j=0; j<size; j++){
            printf(" %d |", matriz[i][j]);
        }
        printf("\n");
    }
    printf("\n");


}

void calculo_paso(int** matriz_visible, int** matriz_support, int size){

    int i;
    int j;
    int i_dos;
    int j_dos;
    int contador_vivos;

    for (i=0; i<size; i++){
        for (j=0; j<size; j++){
            contador_vivos=0;
            //resolvemos caso general
            for (i_dos=i-1;i_dos<=i+1;i_dos++){
                for (j_dos=j-1;j_dos<=j+1;j_dos++){
                    if (i_dos>=size || j_dos>=size || i_dos<0 || j_dos<0 || (i_dos==i && j_dos==j)){
                        continue;
                    }
                    if (matriz_visible[i_dos][j_dos]==1){
                        contador_vivos++;
                    }
                }
            }
            printf("para la posicion [%d][%d] el valor de vivos es= %d \n",i, j, contador_vivos);
            if ((matriz_visible[i][j]==1 && (contador_vivos==2 || contador_vivos==3)) || (matriz_visible[i][j]==0 && contador_vivos==3)){
                matriz_support[i][j]=1;
            }
            else {
                matriz_support[i][j]=0;
            }
        }
    }

}


int main() {
   
    /*

    Reglas del juego de la vida:
    
    Un 1 se convierte en 0 si:
        -A su alrededor hay <2 o >3 1s a su alrededor

    Un 0 se convierte en 1 si:
        -A su alrededor hay 3 1s

    Pasos del juego

    1) Definimos matriz inicial (tamaño que nos indica el usuario), toda llena de 0s

    2) Usuario indica cuales de esas posiciones son 1s

    3) tenemos una matriz con posiciones que son 0 y posiciones que son 1 tal que

    0 | 1 | 0 | 0 | 0
    0 | 0 | 1 | 1 | 0
    1 | 1 | 0 | 0 | 0

    Se resuelve en una matriz aparte qué posiciones se hacen 1 y cuales 0
    (en una matriz aparte porque si no al ir resolviendo modificaríamos la info con la que decidimos si otras celdas deben cambiar o no)



    */


   //comienza ejecucion del programa
   //preguntamos al man que tamaño de matriz quiere

   int size_matriz;
   int i;
   int j;
   

   /* descomentar cuando hayamos perfeccionado el método de entrada
   print("Introduce tamaño matriz: ");
   scanf("%d", tamaño_matriz);


   */

    size_matriz=10;
    //podríamos plantearnos almacenar las matrices en row_major o column_major pero 
    //creo que haré una versión normal y una intentando optimizar por estudiar diferencias de rendimiento en programas random
    //anyways, de momento, se reserva el vector de la fila, y luego en cada posición, se reserva otro vector para las columnas
    //se hace comprobación de errores también
    int **Matriz_visible = (int **) calloc(size_matriz, sizeof(int *));
    int **Matriz_apoyo = (int **) calloc(size_matriz, sizeof(int *));
    if (Matriz_apoyo == NULL || Matriz_visible == NULL){
        printf("Peto reservando las filas");
        return 1;
    }

    for (i=0; i<size_matriz; i++){
        Matriz_visible[i]=(int *)calloc(size_matriz,sizeof(int));
        Matriz_apoyo[i]=(int *)calloc(size_matriz,sizeof(int));
        if (Matriz_visible[i]==NULL || Matriz_apoyo[i]==NULL){
            printf("Peto reservando las columnas");
            return 1;
        }
    }



    //mostramos matriz al usuario y que seleccione cuales quiere poner a 1
    //NI IDEA DE COMO HACER ESO AHORA MISMO ASI QUE VAMOS A TRAMPEAR LA ENTRADA PARA PODER TRABAJAR EN EL MOTOR DE LA SIMULACION

    //ponemos 1s de forma manual en la matriz
    //vamos a copiar el diseño original del juego para poder comprobar
    Matriz_visible[3][4]=1;
    Matriz_visible[3][5]=1;
    Matriz_visible[4][5]=1;
    Matriz_visible[5][5]=1;
    Matriz_visible[5][4]=1;
    Matriz_visible[5][3]=1;

    //printeamos por consola de momento para ver que todo funciona correctamente
    printea_matriz(Matriz_visible, size_matriz);

    //calculo del siguiente paso
    calculo_paso(Matriz_visible, Matriz_apoyo, size_matriz);
    //copiamos la matriz a mano a ver si es eso
    for (i=0; i<size_matriz; i++){
        for (j=0; j<size_matriz;j++){
            Matriz_visible[i][j]=Matriz_apoyo[i][j];
        }
    }
    printf("\n Se ha realizado el calculo del paso y la copia de la matriz \n");

    //volvemos a printear para que se vea el siguiente paso
    printea_matriz(Matriz_visible, size_matriz);

    //liberamos la memoria de las matrices
    //de nuevo, cuando el futuro cambiemos a row-major o lo que sea habrá que alterar esto
    for (i=0; i < size_matriz; i++){
        free(Matriz_apoyo[i]);
        free(Matriz_visible[i]);
    }

    free(Matriz_apoyo);
    free(Matriz_visible);

   return 0;
}