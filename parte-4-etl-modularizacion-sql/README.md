# Parte 4 - ETL modular, SQLite y SQL con Pandas

## Objetivo

Practicar la estructuración de scripts ETL en funciones, almacenar datos limpios en bases de datos y hacer consultas SQL directamente desde Python.

## Contenidos

- Creación de funciones extract(), transform(), load().
- Exportación de datos limpios a una base SQLite.
- Consultas SQL desde Python usando pandas y sqlite3.

## Ejercicios

- `ejercicio1_etl_modular.py`:  
  Crear un ETL completo modularizado por funciones (extract, transform, load).

- `ejercicio2_guardar_sqlite.py`:  
  Guardar un DataFrame en una base de datos SQLite como tabla `ventas`.

- `ejercicio3_sql_desde_pandas.py`:  
  Hacer consultas SQL contra la base `retail.db` desde Python con pandas.

---

## Recomendaciones

- Instalar pandas si no lo hiciste aún (`pip install pandas`).
- Usar sqlite3 (viene incluido con Python).
- Podés inspeccionar la base `retail.db` con herramientas como DB Browser for SQLite o TablePlus.

---

## Recursos útiles

- [Documentación oficial sqlite3 en Python](https://docs.python.org/3/library/sqlite3.html)
- [Documentación de read_sql_query de Pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
