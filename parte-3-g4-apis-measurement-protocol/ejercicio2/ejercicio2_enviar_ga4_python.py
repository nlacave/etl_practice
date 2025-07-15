"""
Ejercicio 2 – Enviar eventos de GA4 desde Python

Objetivo:
Automatizar el envío de eventos de GA4 usando Python y el Measurement Protocol.

Instrucciones:
1. Crear una función llamada send_event() que reciba:
   - measurement_id
   - api_secret
   - client_id
   - nombre del evento
   - parámetros del evento

2. La función debe enviar una solicitud POST a:
   https://www.google-analytics.com/mp/collect

3. El cuerpo del request debe contener:
   {
     "client_id": "...",
     "events": [{ "name": ..., "params": { ... } }]
   }

4. Probar enviando un evento "purchase" con:
   - transaction_id
   - value
   - currency
   - item_name

Bonus:
- Agregar manejo de errores.
- Usar un archivo `.env` para ocultar tus claves.
"""