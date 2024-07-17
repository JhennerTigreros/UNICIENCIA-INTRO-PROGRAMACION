# Descripción del Proyecto

Con el fin de evaluar los conocimientos adquiridos por los estudiantes durante las clases, se plantea el desarrollo de un mini proyecto. Este proyecto se apoyará en los scripts escritos en clases anteriores y permitirá al estudiante organizar, diseñar y utilizar el lenguaje de programación Python de manera sencilla e introductoria.

## Objetivos del Proyecto

El proyecto tiene varios objetivos clave:
1. **Familiarización con Tipos de Datos**: Uso de datos primitivos y compuestos, listas y diccionarios.
2. **Manipulación de Datos**: Implementar un algoritmo que tome como entrada los datos provistos en un archivo CSV.
3. **Operaciones Matemáticas**: Aplicar operaciones matemáticas y de agregación sobre los datos del CSV.
4. **Uso de GitHub**: Subir el proyecto a un repositorio personal en GitHub, explorando así el uso de esta plataforma para proyectos futuros.

## Estructura del Proyecto

El proyecto se divide en las siguientes secciones:

1. **Lectura de Datos**:
    - Leer el archivo CSV proporcionado que contiene operaciones matemáticas básicas (suma, resta, multiplicación, división, potencia).
    - Ejemplo de estructura de archivo:
    ```csv
    operation,operand_1,operand_2
    SUM,232,212
    MUL,12,11
    ...

2. **Procesamiento de Datos**:
    - Cargar los datos en una estructura de datos en Python (lista o diccionario).
    - Implementar funciones para realizar las operaciones matemáticas especificadas en cada fila del CSV.
    - Verificar que los resultados de las operaciones sean correctos y compararlos con los valores provistos en la columna `correct_result`.

3. **Actualización del Archivo CSV**:
    - Modificar el archivo CSV original para incluir los resultados de las operaciones matemáticas realizadas.
    - Asegurarse de que cada fila contenga la operación realizada y su resultado correspondiente.

4. **Subida a GitHub**:
    - Crear un repositorio en GitHub.
    - Subir el proyecto completo incluyendo el archivo CSV modificado, scripts de Python y el archivo README.md.

## Requisitos del Proyecto

Para completar con éxito el proyecto, los estudiantes deberán cumplir con los siguientes requisitos:

1. **Lectura y Procesamiento de Datos**:
    - Leer el archivo CSV proporcionado.
    - Implementar las funciones necesarias para realizar y verificar las operaciones matemáticas.

2. **Actualización del Archivo CSV**:
    - Modificar el archivo CSV original con los resultados correctos de las operaciones.

3. **Repositorio en GitHub**:
    - Crear un repositorio en GitHub y subir todos los archivos del proyecto.
    - Incluir un archivo README.md detallado que explique el proyecto, su estructura y cómo ejecutarlo.

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone https://github.com/JhennerTigreros/UNICIENCIA-INTRO-PROGRAMACION
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd UNICIENCIA-INTRO-PROGRAMACION
    ```
3. Asegúrate de tener instalado Python 3 y crea el directorio `data`
4. Ejecuta el generador de los datos.
    ```sh
    python mini_proyecto-1.py
    ```
5. Revisa el archivo CSV en `data/math_operations.csv`

## Conclusión

Este proyecto permitirá a los estudiantes aplicar los conocimientos adquiridos durante el curso de Python, desarrollando habilidades en la manipulación de datos, la implementación de algoritmos y el uso de GitHub para la gestión de proyectos. ¡Buena suerte!
