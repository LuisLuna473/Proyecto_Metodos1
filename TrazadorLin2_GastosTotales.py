import numpy as np
import matplotlib.pyplot as plt

# Datos originales
años = np.array([2018, 2019, 2020, 2021, 2022, 2023])
gastos = np.array([72174.60, 79963.20, 93629.00, 99064.80, 105735.80, 112464.40])

# Interpolación lineal para los años 2020, 2021, 2022 y 2023
años_interpolacion = [2018, 2019, 2023]  # Tomamos los valores extremos para la interpolación
gastos_interpolacion = [72174.60, 79963.20, 112464.40]  # Gastos de 2018, 2019 y 2023

# Calcular los valores interpolados
gastos_suavizados = np.interp(años, años_interpolacion, gastos_interpolacion)

# Obtener los valores interpolados para los años 2020, 2021, 2022 y 2023
valores_nuevos = {
    2020: gastos_suavizados[np.where(años == 2020)][0],
    2021: gastos_suavizados[np.where(años == 2021)][0],
    2022: gastos_suavizados[np.where(años == 2022)][0],
    2023: gastos_suavizados[np.where(años == 2023)][0]
}

# Mostrar los nuevos valores de 2020, 2021, 2022 y 2023
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