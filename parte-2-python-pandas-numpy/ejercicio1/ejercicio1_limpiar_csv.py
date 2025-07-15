"""
Ejercicio 1 – Limpieza y enriquecimiento de datos

Objetivo:
Cargar el dataset Online Retail, limpiarlo y crear nuevas variables derivadas.

Instrucciones:
1. Cargar el archivo 'Online Retail.csv' usando pandas.
2. Eliminar las filas que tengan valores nulos en las columnas CustomerID, Quantity o UnitPrice.
3. Filtrar únicamente las filas con Quantity > 0 (ventas reales).
4. Crear una nueva columna 'TotalPrice' que sea Quantity * UnitPrice.
5. Mostrar las primeras 10 filas del resultado y las estadísticas básicas (df.describe()).

Tips:
- El archivo puede requerir el encoding 'ISO-8859-1' si da error al abrirlo.
- Revisá bien los tipos de datos de cada columna antes de operar.
"""
