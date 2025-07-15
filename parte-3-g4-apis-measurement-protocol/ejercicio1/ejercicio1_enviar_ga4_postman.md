# Ejercicio 1 – Simular un evento de GA4 usando Postman

## Objetivo
Aprender a enviar manualmente un evento de conversión a GA4 usando el Measurement Protocol y Postman.

## Instrucciones

1. Crear una propiedad en Google Analytics 4 (si no tenés una, creá una propiedad de prueba).
2. Ir a Admin > Data Streams > Web y copiar el `Measurement ID` (por ejemplo: G-XXXXXXXXXX).
3. Obtener el `API Secret`:
   - Admin > Data Streams > Web > Measurement Protocol API > Create API Secret

4. Abrir Postman y realizar una solicitud POST a:

https://www.google-analytics.com/mp/collect?measurement_id=G-XXXXXXXXXX&api_secret=TU_SECRET

1. En el cuerpo de la solicitud, usar el siguiente JSON:

{
  "client_id": "1234567890.1234567890",
  "events": [
    {
      "name": "test_event",
      "params": {
        "test_param": "value",
        "platform": "web"
      }
    }
  ]
}
Verificar que el evento aparece en el DebugView de GA4 (usar una propiedad en modo debug).

Bonus
Cambiar el nombre del evento y agregar parámetros como value, currency, transaction_id.

Usar un client_id real extraído del navegador (desde las cookies de _ga).