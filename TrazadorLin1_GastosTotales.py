import numpy as np
import matplotlib.pyplot as plt

# Datos originales
años = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010])
gastos = np.array([26334.40, 25652.80, 28901.50, 31274.40, 37382.10, 40835.40, 43768.80, 47485.40])

# Interpolación lineal para los años 2004, 2006 y 2009
años_interpolacion = [2003, 2005, 2007, 2010]  # Tomamos los años fuera de los que queremos suavizar
gastos_interpolacion = [26334.40, 28901.50, 37382.10, 47485.40]  # Gastos correspondientes

# Calcular los valores suavizados
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