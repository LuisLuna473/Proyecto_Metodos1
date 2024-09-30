import numpy as np
import matplotlib.pyplot as plt

# Datos originales
años = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010])
gastos = np.array([17896.40, 17472.80, 19813.90, 21614.70, 24782.50, 27314.40, 31685.50, 33656.40])

# Interpolación lineal para los años 2004, 2006 y 2009
años_interpolacion = [2003, 2005, 2007, 2010]  # Tomamos los años de referencia para la interpolación
gastos_interpolacion = [17896.40, 19813.90, 24782.50, 33656.40]  # Gastos correspondientes

# Calcular los valores interpolados
gastos_suavizados = np.interp(años, años_interpolacion, gastos_interpolacion)

# Obtener los valores interpolados para los años 2004, 2006 y 2009
valores_nuevos = {
    2004: gastos_suavizados[np.where(años == 2004)][0],
    2006: gastos_suavizados[np.where(años == 2006)][0],
    2009: gastos_suavizados[np.where(años == 2009)][0]
}

# Mostrar los nuevos valores de 2004, 2006 y 2009
print("Nuevos valores interpolados:")
for año, valor in valores_nuevos.items():
    print(f"Año {año}: {valor:.2f}")

# Graficar los datos originales y suavizados
plt.figure(figsize=(10, 6))

# Graficar los datos originales
plt.plot(años, gastos, 'o-', label="Datos Originales", color='blue')

# Graficar los datos suavizados
plt.plot(años, gastos_suavizados, 's-', label="Datos Suavizados", color='red')

# Etiquetas y título
plt.xlabel('Año')
plt.ylabel('Gastos de Capital (millones)')
plt.title('Gastos de Capital (Originales vs. Suavizados)')
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()