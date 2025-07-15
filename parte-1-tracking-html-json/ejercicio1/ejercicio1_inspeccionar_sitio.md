# Ejercicio 1: Inspeccionar eventos en un sitio web real

**Objetivo:**  
Usar DevTools para analizar cómo se envían eventos de tracking desde un sitio real.

**Pasos:**

1. Abre cualquier sitio web con actividad comercial (ejemplo: <https://www.mercadolibre.com.ar/>).
2. Abre las herramientas de desarrollador (DevTools) con F12 o Ctrl+Shift+I.
3. Ve a la pestaña **Network** y filtra por "collect", "gtm.js" o "pixel".
4. Navega por el sitio y observa las llamadas que se hacen a Google Analytics, Facebook Pixel u otros.
5. Revisa el contenido de estas llamadas (headers, payload).
6. ¿Qué eventos ves? ¿Qué parámetros están enviando?  
7. Abre la pestaña **Console** y prueba:
   - `window.dataLayer`
   - `window.dataLayer.length`
   - `window.dataLayer[0]`  
8. Escribe un pequeño resumen de tus observaciones.

**Entrega:**  
Archivo `.md` con las respuestas y capturas de pantalla opcionales.
