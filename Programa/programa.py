#! /usr/bin/env python
#-*- coding: utf-8 -*-

 #######################################################
 # FILE NAME: InsertionSort.py                         #
 #                                                     #
 # PURPOSE:Programa que se encarga de ordenar una      #
 #         lista de numeros con el algoritmo de        #
 #         InsertionSort                               #
 #                                                     #
 #@author Norma Veronica Trinidad Hernandez            #
 #       <nvth28@gmail.com>                            #
 #                                                     #
 #@author Jose de Jesus Vargas Muñoz                   #
 #        <j.vargas.munoz@gmail.com >                  #
 #                                                     #
 #                                                     #
 #@author Vilchis Dominguez Miguel Alonso              #
 #       <mvilchis@ciencias.unam.mx>                   #
 #                                                     #
 #                                                     #
 # NOTAS: recibe como argumento la longitud de         # 
 #       la primer lista aleatoria que ordenara        #
 #       el segundo argumento es la longitud de la     # 
 #       ultima lista aleatoria que ordenara,se iterara#  
 #       desde la primera hasta la ultima longitud     #    
 #       y los tiempos de ejecucion se almacenaran en  # 
 #       el archivo insertionPython.txt                # 
 #                                                     #
 #                                                     #
 # Copyright (C) 21-08-2015                            # 
 # Distributed under terms of the MIT license.         #
 #######################################################

import sys
import random
import time 
"""*****************************************************
 * FUNCTION NAME: insertionSort                        *
 * PURPOSE: insertion sort, funcion que implementa     *
 *          el algoritmo de insercion                  *
 * ARGUMENTS: length , longitud de la lista a ordenar  *
 *            numbers  lista a ordenar                 *
 * RETURN: void                                        *
 ****************************************************"""

def insertionSort(length, numbers):
    idx = 1
    for idx in range(length):
        key = numbers[idx]
        i = idx-1
        while(i >= 0 and numbers[i] >= key):
            numbers[i+1]= numbers[i]
            i = i-1
        numbers[i+1] = key
"""*****************************************************
 * FUNCTION NAME:createRandom                          *
 * PURPOSE: Crear una lista de numeros aleatorios      *
 * ARGUMENTS: length <int>, longitud de la lista  num  * 
 * RETURN: <int*> numeros a ordenar de longitud length *
 *******************************************************""" 
def createRandom(length):
    numbers =[random.randint(-500000, 500000) for i in range(length)]
    return numbers
def main():
    #Verificación de argumentos
    if (len(sys.argv) != 3 ):
        print("*********************<USO>*******************\n")
        print("Forma de uso, %s #tamInicial #tamFinal\n"%sys.argv[0])
        print ("Donde tamInicial es la longitud de la muestra inicial\n")
        print ("y tamFinal es la logitud de la muestra final\n")
        print("*********************<USO>*******************\n")
        exit(1)
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    f = open('insertionPython.txt', 'w')
    for i  in range(arg1,arg2):
        numbers = createRandom(i)
        begin = time.time()
        insertionSort(i,numbers)
        time_spent = (time.time() - begin)*1000
        for idx in range(i-1):
            assert numbers[idx+1] >= numbers[idx]
        f.write(str(i) + " "+ str(time_spent)+ "\n")
    f.close()
if __name__ == "__main__":
    main()

