"""
Ejercicio 2 – Guardar datos en SQLite desde Pandas

Objetivo:
Persistir el resultado de un ETL en una base de datos SQLite.

Instrucciones:
1. Leer el archivo 'retail_clean.csv' generado en el ejercicio anterior.
2. Crear una conexión a una base de datos SQLite llamada 'retail.db' usando sqlite3.
3. Guardar el DataFrame en una tabla llamada 'ventas', reemplazándola si ya existe.
4. Verificar la creación de la tabla conectándote con un navegador SQLite o leyendo desde código.

Bonus:
- Agregar una verificación de si el archivo CSV existe antes de ejecutar.
- Exportar un pequeño subset (5 filas) para revisión manual como CSV o JSON.
"""
