import numpy as np

# Datos proporcionados
años = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
                 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
                 2021, 2022, 2023])
gastos_corrientes = np.array([17896.40, 18855.15, 19813.90, 22298.20, 24782.50, 27314.40, 
                               30698.43, 33656.40, 34713.20, 38738.90, 40189.60, 42215.80, 
                               44477.40, 46198.60, 49355.80, 52788.50, 58365.90, 64062.83, 
                               69759.75, 75456.68, 81153.60])

# Ajustar un polinomio de grado 3
coeficientes = np.polyfit(años, gastos_corrientes, 3)

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

