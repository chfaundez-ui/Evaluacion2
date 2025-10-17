# Evaluacion2
Proyecto en Python para la Biblioteca Nacional que calcula rutas optimizadas entre dos ubicaciones usando la API de GraphHopper. Permite obtener coordenadas geográficas, distancia total, tiempo estimado y direcciones paso a paso, facilitando a los visitantes planificar su llegada de manera eficiente y rápida.
INSTRUCCIONES:
1. Requisitos previos
- Tener instalado Python 3.
- Instalar la librería requests si no está presente:
  pip install requests

2. Clonar o descargar el proyecto
- Clonar el repositorio:
  git clone <URL_DEL_REPOSITORIO>
- Entrar a la carpeta del proyecto:
  cd <NOMBRE_DEL_PROYECTO>

3. Ejecutar el script
- En la terminal o consola, ejecutar:
  python nombre_del_script.py
  (Reemplaza nombre_del_script.py por el nombre real del archivo Python.)

4. Uso del programa
- Se pedirá ingresar la ubicación de inicio.
- Luego, ingresar la ubicación de destino.
- El programa mostrará:
  - Distancia total (km y millas)
  - Tiempo estimado del viaje
  - Instrucciones paso a paso del recorrido

5. Finalizar
- Puedes escribir 'salir' o 's' en cualquier momento para terminar la ejecución.
"""

# Guardar en un archivo
ruta_archivo = '/mnt/data/instrucciones.txt'
with open(ruta_archivo, 'w') as file:
    file.write(instrucciones)

ruta_archivo
