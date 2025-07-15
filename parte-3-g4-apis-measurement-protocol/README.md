# Parte 3 - GA4, APIs y Measurement Protocol

## Objetivo
Aprender a enviar eventos a Google Analytics 4 usando el Measurement Protocol y trabajar con datos de tracking en formato JSON.

## Contenidos

- Envío manual de eventos a GA4 usando Postman.
- Automatización del tracking con Python (enviar eventos programáticamente).
- Lectura y procesamiento de datos de eventos simulados para análisis.

## Ejercicios

- `ejercicio1_enviar_ga4_postman.md`:  
  Enviar eventos personalizados a GA4 vía Postman, utilizando el Measurement Protocol.

- `ejercicio2_enviar_ga4_python.py`:  
  Crear un script en Python que envíe eventos GA4 usando requests y claves API.

- `ejercicio3_parsear_eventos.py`:  
  Leer y analizar un archivo JSON con eventos simulados, y transformarlo a DataFrame.

---

## Recomendaciones

- Tener acceso a una propiedad GA4 y API Secret.
- Usar Postman para probar requests de manera visual.
- Instalar `requests`, `pandas`, `python-dotenv` si querés usar un `.env`.

---

## Recursos útiles

- [GA4 Measurement Protocol docs](https://developers.google.com/analytics/devguides/collection/protocol/ga4)
- [Cómo obtener el API Secret de GA4](https://support.google.com/analytics/answer/9267744)
