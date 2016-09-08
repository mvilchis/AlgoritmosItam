#! /bash/bin

#############################################
# Programa que implementa el metodo simplex #
#          			            #
# @autho Vilchis Dominguez Miguel Alonso    #
#        mvilchis@ciencias.unam.mx          #
#					    #
# @version 1.0                              #
#############################################

import sys
solution = {} #Diccionario que guardara los movimientos de x_i, de columnas a renglones
l_solution = [] #Lista de listas que tendra la coordenada del cambio hecho 


# Funcion que regresa el indice de menor valor en una lista 
def get_min_idx(values):
    return values.index(min(values))


#Funcion que regresa el indice del pivote para las columna
#segun la especificacion del metodo simplex 
def get_column_pivot_index(table):
    last_idx = len(table)-1
    return get_min_idx(table[last_idx])

#Funcion que regresa el indice del pivote para los renglones
#segun la especificacion del metodo simplex 
def get_row_pivot_index(table, pivot_idx):
    last_idx = len(table[0])-1
    #Dividimos la ultima columna por el pivote 
    last_col = [row[last_idx]/float(row[pivot_idx])  for row in table if row[pivot_idx]!= 0]
    last_col_aux = []
    for l in last_col:
       if l < 0:
          last_col_aux.append(1000000000000) #No consideramos los denominadores negativos para index col 
       else:
          last_col_aux.append(l)
    return get_min_idx(last_col_aux[0:-1]) #El ultimo valor es el de B, no lo tomamos en cuenta

# Si se trata del renglon que se escogio como pivote,  se regresa la columna como renglon 
# Si no, se calcula el nuevo renglon con el algoritmo simplex 
def update_row (table, idx, col_pivot, row_pivot, new_pivot_row):
    if idx == row_pivot:
       global solution
       solution[col_pivot] = idx
       l_solution.append([row_pivot, col_pivot])
       return new_pivot_row
    else:
       old_row = table[idx]
       element = old_row[col_pivot]
       return [old - new*element for old, new in zip(old_row,new_pivot_row)]
      
# Funcion que realiza una iteracion a la tabla 
#segun la especificacion del metodo simplex  
def update_table (table,col_pivot,row_pivot):
    element = table[row_pivot][col_pivot]
    {}
    new_pivot_row = [e / float(element) for e in table[row_pivot]]
    for idx in range(len(table)):
       table[idx] = update_row(table, idx, col_pivot, row_pivot, new_pivot_row)

#Funcion que crea la tabla     
def create_table(A,B,C):
    total_inequation =len(B)
    x_i = len(C)
    counter = 0
    table = []
    #Creamos la tabla para las x_i Basicas 
    for i in range(0, total_inequation):
        l = A[counter] #Desigualdad i
        aux_array = [0]*total_inequation #Arreglo de 0 
        aux_array[counter] = 1 #Modificamos i en la columna
        table.append(l+aux_array +[B[counter]])
        counter +=1
    #Agregamos la fila para la soluciones 
    l = [c*-1 for c in C]
    aux_array = [0]*total_inequation
    table.append(l+aux_array+[0]) 
    return table

#Funcion que revisa si todos los elementos de la lista 
# son positivos, es decir, si ya se llego al optimo
def satisfy_condition(table):
    last_idx = len(table)-1 
    for item in table[last_idx]:
       if item < 0:
          return False
    return True

#Funcion que agrega ceros  a toda una columna, y 1 
#en el renglo que se utilizo
def zero_column(table, col_pivot, row_pivot):
    for idx in range(len(table)):
        table[idx][col_pivot] = 0
    table[row_pivot][col_pivot] = 1

# Funcion que imprime la tabla con la que se trabaja
def print_matrix(table):
    for i in table:
      for j in i:
         print "%.2f"%(j),
      print ""
#Metodo simplex 
def simplex(A,B,C):
    table = create_table(A,B,C)
    global l_solution
    global solution
    solution = {}
    l_solution = []
    counter = 0
    while(not satisfy_condition(table)):
      c_pivot = get_column_pivot_index(table)
      r_pivot = get_row_pivot_index(table, c_pivot)
      update_table(table, c_pivot, r_pivot)
      for j in l_solution:
          zero_column(table, j[1], j[0])
      print "-"*10 + " Tabla en la iteracion %i" %(counter) + "-"*10
      print_matrix( table)
      counter += 1
    result = []
    final_string = "\nLa solucion esta dada por :\n"
    counter = 0
    for i in range(len(C)):
       if i in solution.keys():
         idx = solution[i]
         sol = table[idx][-1:]
         final_string += "x_%d: %.2f \n" %(counter, sol[0])
       else:
         final_string += "x_%d: 0 \n" %(counter)
       counter += 1
    
    return final_string

#Ejemplo prueba
A = [[4,2], [8,8], [0,2]]
B = [20,20,10]
C = [10,20] 
print simplex(A,B,C)
#Ejemplo visto en clase
A = [[2,3], [4,1], [2,9]]
B = [25,32,54]
C= [21,31]
print simplex(A,B,C)
