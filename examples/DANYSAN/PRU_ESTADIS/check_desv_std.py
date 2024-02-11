import numpy as np
from scipy.stats import chisquare

# Ejemplo de datos
datos = np.array([2, 5, 3, 8, 6, 4, 7, 1])

# Desviación estándar
desviacion_estandar = np.std(datos)
print("Desviación Estándar:", desviacion_estandar)

# Prueba de chi-cuadrado
frecuencia_obs, _ = np.histogram(datos, bins=3)  # Ajusta el número de bins según tu necesidad
frecuencia_esp = np.ones_like(frecuencia_obs) * len(datos) / len(frecuencia_obs)
chi_cuadrado, p_valor = chisquare(frecuencia_obs, frecuencia_esp)

print("Chi-Cuadrado:", chi_cuadrado)
print("Valor p:", p_valor)



