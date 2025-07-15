"""
Ejercicio 3 – Consultas SQL con Pandas

Objetivo:
Practicar consultas SQL sobre un DataFrame o directamente contra SQLite.

Instrucciones:
1. Conectar a la base de datos 'retail.db' creada anteriormente.
2. Usar pandas.read_sql_query() para ejecutar las siguientes consultas:

   a. Total de ventas por país (`SUM(TotalPrice)`)
   b. Cantidad de facturas únicas por país (`COUNT(DISTINCT InvoiceNo)`)
   c. Top 5 clientes que más gastaron

3. Mostrar los resultados por consola y exportar uno de ellos como CSV.

Bonus:
- Usar sqlite3 + pandasql (opcional) si querés practicar consultas sobre DataFrames en memoria.
"""
