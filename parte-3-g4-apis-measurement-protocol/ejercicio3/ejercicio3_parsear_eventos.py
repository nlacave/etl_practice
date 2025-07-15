"""
Ejercicio 3 – Parsear datos de eventos en formato JSON

Objetivo:
Simular la lectura de eventos enviados por una API de tracking y transformarlos para análisis.

Instrucciones:
1. Crear un archivo JSON que contenga una lista de eventos GA4 simulados con campos como:
   - event_name
   - client_id
   - timestamp
   - value
   - currency

2. Cargar el archivo con `json.load()` y guardarlo como una lista de diccionarios.

3. Convertir esa lista a un DataFrame de Pandas.

4. Calcular:
   - Total de eventos por tipo (`event_name`)
   - Suma total de `value` por cliente
   - Eventos ordenados por fecha

Bonus:
- Convertir el campo `timestamp` a datetime con `pd.to_datetime`.
- Guardar el resultado final como CSV.
"""
