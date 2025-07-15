"""
Ejercicio 3 – Mini ETL por país

Objetivo:
Simular un pipeline de procesamiento de ventas agrupado por país.

Instrucciones:
1. Usar el dataset limpio de los ejercicios anteriores.
2. Agrupar los datos por 'Country' y calcular por país:
   - Total de ventas (suma de TotalPrice)
   - Cantidad de clientes únicos
   - Cantidad total de facturas (InvoiceNo únicos)
3. Ordenar los resultados por total de ventas, de mayor a menor.
4. Exportar el dataframe final a un nuevo archivo CSV llamado 'ventas_por_pais.csv'.

Bonus:
- Convertí este script en funciones tipo extract(), transform(), load().
- Podés generar un gráfico de los 10 países con más ventas si querés practicar visualización.
"""
