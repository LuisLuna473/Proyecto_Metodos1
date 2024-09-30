import numpy as np

# Datos proporcionados
años = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
                 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
                 2021, 2022, 2023])
gastos = np.array([26334.40, 27617.95, 28901.50, 33141.80, 37382.10, 40835.40, 
                   44117.63, 47485.40, 48954.40, 53111.60, 55310.60, 58249.00, 
                   60883.30, 63814.70, 67710.60, 72174.60, 79963.20, 88088.50, 
                   96213.80, 104339.10, 112464.40])

# Ajustar un polinomio de grado 3
coeficientes = np.polyfit(años, gastos, 3)

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


