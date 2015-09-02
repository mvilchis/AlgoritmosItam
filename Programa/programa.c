/*******************************************************
 *******************************************************/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

void iteracion (int n) {
    int i, j, k, x = 0;
    for (i = 1; i < n; i++) {
        for (j = 1 ; j < i; j++){
            for(k = 1; k < i; k++)
                x = x+1;
        }
    }
}


int main(int argc, char **argv) {
    //Declaracion de variables 
    int ret1, ret2; //Control de parseo
    int arg1, arg2, arg3; //Parseo de argumento
    FILE *file; //Archivo para guardar tiempo de ejecucion
    double time_spent; //Variable que guarda el tiempo neto de ejecucion
    int *numbers; //Lista temporal de secuencia de numeros
    int i, counter; //Indices auxiliares 

    //Verificación de argumentos
    if (argc != 3 ) {
        printf("*********************<USO>*******************\n");
        printf("Forma de uso, %s #tamInicial #tamFinal \n",argv[0]);
        printf("Donde tamInicial es la longitud de la muestra inicial\n");
        printf("y tamFinal es la longitud de la muestra final\n");
        printf("*********************<USO>*******************\n");
        exit(1);
    }

    ret1 = sscanf(argv[1], "%d", &arg1);
    ret2 = sscanf(argv[2], "%d", &arg2);
    if (ret1  != 1 || ret2 != 1 ) {
        printf("*********************<ERROR>*******************\n");
        printf("Error al leer los parametros, recuerda que son numeros\n");
        printf("*********************<ERROR>*******************\n");

    }
    file = fopen("C.txt", "w");
    if (file == NULL) {
        printf("Error al abrir el archivo\n");
        exit(1);
    }
    for(counter = arg1; counter < arg2; counter++) {
        clock_t begin, end; //Inicio y final del tiempo de ejecucion
        begin = clock();
        iteracion(counter);
        end = clock();
        time_spent = ((double)(end - begin) / CLOCKS_PER_SEC )*1000000; 
        fprintf(file, "{%d ,%lf},", counter,time_spent);
    }
    fclose(file);
} 
