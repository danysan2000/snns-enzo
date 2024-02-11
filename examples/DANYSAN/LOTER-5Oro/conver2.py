import pandas as pd
import numpy as np

# Tu vector de elementos
vector_elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Puedes cambiar estos valores

# Calcula el número de filas necesario para acomodar todos los elementos en grupos de 5 columnas
num_filas = len(vector_elementos) // 5 + (1 if len(vector_elementos) % 5 > 0 else 0)

# Crea una matriz vacía con 5 columnas y el número calculado de filas
matriz = pd.DataFrame(np.zeros((num_filas, 5)))

# Reformatea el vector para que coincida con la forma de la matriz
vector_reformateado = np.array(vector_elementos).reshape(-1, 5)

# Copia los elementos reformateados del vector a la matriz
matriz.iloc[:vector_reformateado.shape[0], :vector_reformateado.shape[1]] = vector_reformateado

# Imprime la matriz resultante
print(matriz)

