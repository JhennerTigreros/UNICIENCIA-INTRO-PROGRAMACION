# Proyecto de Batallas entre Pokémons

## Descripción del Proyecto

El objetivo de este proyecto es evaluar los conocimientos adquiridos en programación orientada a objetos (OOP) a través de la implementación de una aplicación de consola que permita realizar batallas entre pokémons. Los estudiantes deberán implementar un sistema que permita agregar, modificar y eliminar pokémons de manera flexible y dinámica, utilizando las técnicas aprendidas durante el curso.

## Requisitos del Proyecto

1. **Implementación de Pokémons**:
   - Cada Pokémon debe tener una tarjeta con sus características intrínsecas, como nombre, tipo, estadísticas de combate, entre otras.
   - El estudiante debe utilizar la información del archivo `pokemon.csv` para crear las tarjetas de Pokémon.

2. **Operaciones sobre Pokémons**:
   - Agregar nuevos pokémons.
   - Modificar las características de los pokémons existentes.
   - Eliminar pokémons del sistema.

3. **Batallas entre Pokémons**:
   - Implementar una funcionalidad que permita simular batallas entre dos pokémons.
   - Definir reglas y condiciones para determinar el ganador de una batalla.

4. **Repositorio en GitHub**:
   - Subir el proyecto en forma de repositorio en una cuenta personal de GitHub.
   - El proyecto debe ser descargable e instalable usando la herramienta PIP.

## Uso del archivo `pokemon.csv`

El archivo `pokemon.csv` contiene información detallada de varios pokémons que se utilizará para inicializar el sistema. A continuación se muestra un ejemplo de cómo leer y utilizar los datos del archivo:

```python
import pandas as pd

# Cargar datos desde el archivo CSV
pokemon_data = pd.read_csv('pokemon.csv')

# Mostrar los primeros 5 registros para verificar la carga de datos
print(pokemon_data.head())
```


## Evaluación

El proyecto será evaluado con base en los siguientes criterios:

- Correcta implementación de las clases y métodos utilizando OOP.
- Flexibilidad y dinamismo en la gestión de pokémons.
- Funcionalidad y lógica de las batallas entre pokémons.
- Calidad del código y documentación.
- Correcta configuración del repositorio y facilidad de instalación.

## Notas Finales

- Asegúrese de seguir las mejores prácticas de codificación y documentación.
- Realice pruebas exhaustivas para garantizar el correcto funcionamiento del sistema.
- Mantenga su repositorio actualizado y documentado para facilitar futuras contribuciones.

¡Buena suerte y diviértase desarrollando su sistema de batallas de pokémons!
