"""
Ejercicio 1 – Modularizar un proceso ETL

Objetivo:
Organizar un proceso ETL completo en funciones reutilizables.

Instrucciones:
1. Usar el dataset limpio del Online Retail (o volver a cargarlo y limpiarlo dentro del script).
2. Crear una función extract() que cargue el archivo 'Online Retail.csv'.
3. Crear una función transform(df) que:
   - Elimine nulos en CustomerID
   - Filtre Quantity > 0
   - Calcule 'TotalPrice' = Quantity * UnitPrice
4. Crear una función load(df) que exporte el resultado limpio a un nuevo archivo 'retail_clean.csv'.

Bonus:
- Agregar logging (print/logs) para saber en qué etapa está el script.
- Agregar un parámetro para cambiar el nombre del archivo de salida.
"""
