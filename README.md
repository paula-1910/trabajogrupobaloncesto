# trabajogrupobaloncesto
 Batit CarlosM y PaulaM
 
Este código permite planificar sesiones de entrenamiento para un grupo de jugadores, distribuyendo su tiempo en diferentes áreas de mejora, respetando tiempos máximos por jugador y tiempo total disponible. Al finalizar, se muestra un resumen de las mejoras y un gráfico radar con el progreso de cada jugador.

Antes de ejecutar este script, asegúrate de tener instaladas las siguientes librerías de Python:
matplotlib
numpy

Para ejecutarlo:
1. Guarda el código en un archivo, por ejemplo: `plan_entrenamiento.py`.
2. Abre una terminal o consola en la carpeta donde guardaste el archivo.
3. Ejecuta el script con: python plan_entrenamiento.py

El script te pedirá información mediante la terminal:
¿Cuántos jugadores hay? Ingresa un número entero positivo.
Y por cada jugador, 
- Nombre del jugador (único y no vacío)
- Nivel inicial en cada área de entrenamiento, en una escala del 1 al 5:
  - tiros
  - defensa
  - condicion
  - dribling

Una vez ingresados todos los datos, el programa:

1. Asigna sesiones de entrenamiento de forma automática respetando:
   - Tiempo total disponible
   - Tiempo máximo por jugador
   - Máximo nivel de habilidad (5)

2. Muestra:
   - Detalle de cada sesión asignada
   - Plan de entrenamiento completo
   - Habilidades finales de cada jugador
   - Mejoras por área
   - Análisis de eficiencia (mejoras por minuto)
   - Eficiencia global del equipo

3. Genera un gráfico radar donde se visualiza:
   - Habilidades iniciales (línea discontinua)
   - Habilidades finales (línea continua)
   - Comparación por jugador y por área

 Notas
- Los niveles de habilidad no pueden superar 5.
- No se asignarán más sesiones a un jugador que ya haya alcanzado el máximo de habilidades o su límite de tiempo.
- El programa asegura un reparto eficiente del tiempo y prioriza las áreas con menor nivel.
