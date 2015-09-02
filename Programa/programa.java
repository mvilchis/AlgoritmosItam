import java.util.Random;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
/**
 * FILE NAME: InsertionSort.java                           
 *                                                     
 * PURPOSE:Programa que se encarga de ordenar una      
 *         lista de numeros con el algoritmo de        
 *         InsertionSort                                   
 *                                                     
 *@author Norma Veronica Trinidad Hernandez            
 *       <nvth28@gmail.com>                            
 *                                                     
 *@author Jose de Jesus Vargas Muñoz                   
 *        <j.vargas.munoz@gmail.com >                  
 *                                                     
 *                                                     
 *@author Vilchis Dominguez Miguel Alonso              
 *       <mvilchis@ciencias.unam.mx>                   
 *                                                     
 *                                                     
 * NOTES: recibe como argumento la longitud de         
 *       la primer lista aleatoria que ordenara        
 *       el segundo argumento es la longitud de la     
 *       ultima lista aleatoria que ordenara,se iterara
 *       desde la primera hasta la ultima longitud     
 *       y los tiempos de ejecucion se almacenaran en  
 *       el archivo insertionJava.txt                     
 *                                                     
 * Copyright (C) 21-08-2015                            
 * Distributed under terms of the MIT license.      
 */ 


public class InsertionSort {
    /** Constructor por defecto */
    public InsertionSort() { }
    /**
     * Metodo que implementa el algoritmo de insercion 
     * @param length <int>, longitud de la lista a ordenar
     * @param numbers <int[]> lista a ordenar          
     */ 
    public void insertionSort(int length, int numbers[]) {
        int idx = 1, i;
        int key;
        for(idx = 1; idx < length; idx++) {
            key = numbers[idx];
            i = idx-1;
            while (i >= 0 && numbers[i] >= key) {
                numbers[i+1] = numbers[i];
                i--;
            }
            numbers[i+1] = key;
        }
    }

    /**
     *Metodo que crea una lista de numeros aleatorios    
     *@param length <int>, longitud de la lista  num 
     *@param rnd <Random> generador de numeros random
     * @return  <int[]> numeros a ordenar de longitud length 
     */  
    public int[] createRandom(int length, Random rnd) {
        int numbers[] = new int [length];
        int idx = 0;
        for(idx = 0; idx < length; idx++) {
            numbers [idx] = rnd.nextInt();
        }
        return numbers;

    }
    public static void  main(String [] args) {
        //Declaracion de variables 
        int arg1=0, arg2=0; //Parseo de argumento
        int i, idx; //Indices auxiliares
        int argc = args.length;
        double time_spent, begin;
        int numbers[];
        Random rnd = new Random();
        InsertionSort algorithm = new InsertionSort(); 

        //Verificación de argumentos
        if (argc != 2 ) {
            System.out.print("*********************<USO>*******************\n");
            System.out.print("Forma de uso java MergeSort #tamIncial #tamFinal\n" );
            System.out.print("Donde tamInicial es la longitud de la muestra inicial\n");
            System.out.print("y tamFinal es la longitud de la muestra final \n");
            System.out.print("*********************<USO>*******************\n");
            System.exit(1);
        }

        try{
            arg1 = Integer.parseInt(args[0]);
            arg2 = Integer.parseInt(args[1]);

        } catch (NumberFormatException e) {
            System.out.print("*********************<ERROR>*******************\n");
            System.out.print("Error al leer los parametros, recuerda que son numeros\n");
            System.out.print("*********************<ERROR>*******************\n");
            System.exit(1);

        } 
        try {
            File file = new File("insertionJava.txt");

            if (!file.exists()) {
                file.createNewFile();
            }

            FileWriter fw = new FileWriter(file.getAbsoluteFile());
            BufferedWriter bw = new BufferedWriter(fw);

            for(int counter = arg1; counter < arg2; counter++) {
                numbers = algorithm.createRandom(counter,rnd);
                begin = System.nanoTime();
                algorithm.insertionSort(counter, numbers);

                time_spent = (System.nanoTime() - begin)/1000000; //Milisegundos

                for(i = 0; i < counter-1; i++)
                    assert(numbers[i+1]) >= (numbers[ i]);
                bw.write(counter+ " "+time_spent+"\n");
            } 
            bw.close(); 
        } catch (IOException e) {
            e.printStackTrace();
        } 
    }
} 
