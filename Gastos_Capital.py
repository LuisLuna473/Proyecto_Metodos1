import numpy as np

# Datos proporcionados
años = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
                 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
                 2021, 2022, 2023])
gastos_capital = np.array([8438.80, 9085.80, 9732.80, 11166.20, 12599.60, 13521.00, 
                           13625.05, 13729.10, 14241.20, 14372.80, 15121.00, 16033.20, 
                           16405.90, 17616.10, 18354.80, 19386.10, 21597.30, 24025.67, 
                           26454.05, 28882.42, 31310.80])

# Ajustar un polinomio de grado 3
coeficientes = np.polyfit(años, gastos_capital, 3)

# Crear un objeto polinómico
polinomio = np.poly1d(coeficientes)

# Función para evaluar el polinomio
def evaluar_en_año(año):
    return polinomio(año)

# Evaluaciones para los años 2024 y 2025
año_2024 = 2024
año_2025 = 2025

gasto_estimado_2024 = evaluar_en_año(año_2024)
gasto_estimado_2025 = evaluar_en_año(año_2025)

# Imprimir el polinomio
print("Polinomio de Lagrange (grado 3):")
print(polinomio)

# Imprimir los gastos estimados
print(f"Gasto estimado para el año {año_2024}: {gasto_estimado_2024:.2f}")
print(f"Gasto estimado para el año {año_2025}: {gasto_estimado_2025:.2f}")

