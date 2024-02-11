#
# convertir vector tabla 5 de oro a matriz de x por 5(col)
#
#

import pandas as pd
import numpy as np

   # Tu vector de elementos
vector_elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15]  # Puedes cambiar estos valores
print(vector_elementos)
vec_ax = np.array(vector_elementos)
vec_ax2 = vec_ax.reshape(3,5)

   # Calcula el número de filas necesario para acomodar todos los elementos en grupos de 5 columnas
num_filas = len(vector_elementos) // 5 + (1 if len(vector_elementos) % 5 > 0 else 0)
print(num_filas)

   # Crea una matriz vacía con 5 columnas y el número calculado de filas
matriz = pd.DataFrame(np.zeros((num_filas, 5)))
print(matriz)

   # Copia los elementos del vector a la matriz
#matriz.iloc[:len(vector_elementos), :(len(vector_elementos) % 5)] = vector_elementos
matriz.iloc[:(num_filas-1) , :(len(vector_elementos) % 5)] = vec_ax2

   # Imprime la matriz resultante
print(matriz)



