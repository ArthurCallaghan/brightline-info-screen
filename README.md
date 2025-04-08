# Brightline Info Screen

Pantalla informativa para salidas de trenes de Brightline desde MiamiCentral.

## Archivos

- `pantalla-brightline.html`: pantalla visual con los próximos trenes.
- `scraper.py`: script que extrae los horarios reales.
- `trenes.json`: archivo con los datos usados por la pantalla.
- `render.yaml`: configuración para desplegar en Render.com

## Cómo usar en Render

1. Sube estos archivos a un repositorio en GitHub.
2. Ve a https://render.com y crea un nuevo Blueprint Service.
3. Elige tu repositorio y Render desplegará:
   - Un sitio estático con `pantalla-brightline.html`.
   - Un cron job que ejecuta `scraper.py` cada 10 minutos.
"# brightline-info-screen" 
