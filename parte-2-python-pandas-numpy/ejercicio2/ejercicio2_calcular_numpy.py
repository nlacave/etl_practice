"""
Ejercicio 2 – Clasificación de clientes con NumPy

Objetivo:
Etiquetar a los clientes en función de cuánto gastaron.

Instrucciones:
1. Usar el dataframe limpio del ejercicio anterior, o generar uno nuevo con CustomerID y TotalPrice acumulado.
2. Calcular el total gastado por cada cliente (groupby CustomerID + sum).
3. Usar numpy.where() o numpy.select() para crear una columna llamada 'segmento_cliente':
   - 'Alta' si gastó más de 1000
   - 'Media' si gastó entre 500 y 1000
   - 'Baja' si gastó menos de 500
4. Mostrar el resultado ordenado por total gastado (de mayor a menor).

Tips:
- Importá numpy como np.
- Usá .merge() si querés reutilizar el dataframe del ejercicio 1 y sumar columnas.
"""
