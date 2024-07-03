# Configuración de Proyecto con Python y Visual Studio Code

Este documento ofrece una guía completa para configurar un proyecto de Python utilizando Visual Studio Code (VS Code) y el entorno virtual venv en sistemas operativos Mac, Windows y Linux. Además, se incluye una sección sobre el uso de la terminal y comandos básicos para cada sistema operativo.

## Índice

1. [Terminal y Comandos Básicos](#terminal-y-comandos-básicos)
   - [Mac](#mac)
   - [Windows](#windows)
   - [Linux](#linux)
2. [Instalación de Visual Studio Code](#instalación-de-visual-studio-code)
3. [Instalación de Python](#instalación-de-python)
   - [Mac](#instalación-de-python-en-mac)
   - [Windows](#instalación-de-python-en-windows)
   - [Linux](#instalación-de-python-en-linux)
4. [Configuración de Visual Studio Code para Python](#configuración-de-visual-studio-code-para-python)
5. [Configuración del Entorno Virtual (venv)](#configuración-del-entorno-virtual-venv)

---

## Terminal y Comandos Básicos

### Windows

En Windows, la terminal puede ser el Símbolo del sistema (CMD) o PowerShell. Ambas herramientas permiten ejecutar comandos para gestionar archivos y directorios.

#### Comandos Básicos

- **Abrir CMD**: Puedes abrir el Símbolo del sistema buscando "cmd" en el menú de inicio.
- **Abrir PowerShell**: Puedes abrir PowerShell buscando "PowerShell" en el menú de inicio.
- **Navegar entre directorios**:
  ```sh
  cd nombre_del_directorio
  ```
- **Listar archivos y directorios**:
  ```sh
  dir
  ```
- **Crear un directorio**:
  ```sh
  mkdir nombre_del_directorio
  ```
- **Crear un archivo**:
  ```sh
  echo. > nombre_del_archivo
  ```

### Linux

La terminal en Linux es similar a la de Mac y se puede acceder a ella desde el menú de aplicaciones o utilizando combinaciones de teclas específicas. Es una herramienta esencial para cualquier usuario de Linux.

#### Comandos Básicos

- **Abrir la Terminal**: Puedes abrir la terminal buscando "Terminal" en el menú de aplicaciones.
- **Navegar entre directorios**:
  ```sh
  cd nombre_del_directorio
  ```
- **Listar archivos y directorios**:
  ```sh
  ls
  ```
- **Crear un directorio**:
  ```sh
  mkdir nombre_del_directorio
  ```
- **Crear un archivo**:
  ```sh
  touch nombre_del_archivo
  ```


### Mac

La terminal en Mac es una herramienta poderosa que permite a los usuarios interactuar con el sistema operativo mediante comandos de texto. A continuación, se presentan algunos comandos básicos que te ayudarán a navegar y gestionar archivos y directorios.

#### Comandos Básicos

- **Abrir la Terminal**: Puedes abrir la terminal buscando "Terminal" en Spotlight o navegando a Aplicaciones > Utilidades > Terminal.
- **Navegar entre directorios**:
  ```sh
  cd nombre_del_directorio
  ```
- **Listar archivos y directorios**:
  ```sh
  ls
  ```
- **Crear un directorio**:
  ```sh
  mkdir nombre_del_directorio
  ```
- **Crear un archivo**:
  ```sh
  touch nombre_del_archivo
  ```

---

## Instalación de Visual Studio Code

Visual Studio Code es un editor de código fuente desarrollado por Microsoft. Es ligero pero potente, y soporta una amplia gama de lenguajes de programación, incluyendo Python.

1. Descarga Visual Studio Code desde su [sitio oficial](https://code.visualstudio.com/).
2. Ejecuta el instalador y sigue las instrucciones en pantalla para completar la instalación.

---

## Instalación de Python

Python es un lenguaje de programación interpretado, interactivo y orientado a objetos. A continuación, se detallan los pasos para instalar Python en diferentes sistemas operativos.

### Instalación de Python en Windows

1. Descarga el instalador de Python desde [python.org](https://www.python.org/downloads/).
2. Ejecuta el instalador y asegúrate de marcar la opción "Add Python to PATH".
3. Sigue las instrucciones del instalador.
4. Verifica la instalación abriendo el Símbolo del sistema (CMD) y ejecutando:
    ```sh
    python --version
    ```

### Instalación de Python en Mac

1. Abre la terminal.
2. Instala Homebrew (si no lo tienes instalado) con el siguiente comando:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
3. Instala Python usando Homebrew:
    ```sh
    brew install python
    ```
4. Verifica la instalación ejecutando:
    ```sh
    python3 --version
    ```


### Instalación de Python en Linux

1. Abre una terminal.
2. Usa el gestor de paquetes de tu distribución para instalar Python. Por ejemplo, en Debian/Ubuntu:
    ```sh
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```
3. Verifica la instalación ejecutando:
    ```sh
    python3 --version
    ```

---

## Configuración de Visual Studio Code para Python

Para desarrollar en Python con Visual Studio Code, es necesario configurar algunas extensiones y ajustes.

1. Abre Visual Studio Code.
2. Instala la extensión de Python de Microsoft:
    - Ve a la pestaña de Extensiones (icono de cuadrados en la barra lateral izquierda).
    - Busca "Python" y selecciona la extensión desarrollada por Microsoft.
    - Haz clic en "Instalar".

3. Configura el intérprete de Python:
    - Abre la Paleta de Comandos (Ctrl+Shift+P o Cmd+Shift+P en Mac).
    - Escribe "Python: Select Interpreter" y selecciona el intérprete de Python que deseas usar.

---

## Configuración del Entorno Virtual (venv)

El uso de entornos virtuales es una práctica recomendada para gestionar dependencias en proyectos de Python. A continuación, se detallan los pasos para configurar un entorno virtual en VS Code.

0. Al momento de abrir VSCode selección la opción archivo en la parte superior izquierda y selecciona abrir carpeta, y selecciona la carpeta donde guardaras tus archivos.

1. Abre una terminal integrada en VS Code (Ctrl+`).

2. Verifica que estas en el ruta del proyecto.
   ```sh
   pwd
   ```
   este comando debería darte la ruta actual valida si es la misma carpeta que aparece en tu proyecto.
3. Navega al directorio de tu proyecto:
    ```sh
    cd ruta/a/tu/proyecto
    ```
4. Crea un entorno virtual, usando la utilidad de python que ya instalaste y el flag `-m` y el modulo venv, importante el segundo venv es el nombre de la carpeta que te creara con el entorno virtual.
    ```sh
    python3 -m venv venv
    ```
    En Windows, puedes usar:
    ```sh
    python -m venv venv
    ```
5. Activa el entorno virtual:
    - En Mac/Linux:
        ```sh
        source venv/bin/activate
        ```
    - En Windows:
        ```sh
        .\venv\Scripts\activate
        ```
6. Verifica que el entorno virtual está activado. Deberías ver el nombre del entorno (venv) al inicio de tu línea de comandos.
7. Instala las dependencias necesarias utilizando pip:
    ```sh
    pip install -r requirements.txt
    ```

---

## Estructura del Proyecto

A continuación, se muestra una estructura de directorios recomendada para tu proyecto de Python. Esta estructura facilita la organización y gestión del código y las dependencias.

```bash
├── intro_python
│   ├── clase_1
│   │   └── sintaxis.py
│   └── clase_2
│       └── control.py
├── lbrerias
│   ├── mathlib
│   │   ├── mathlib
│   │   │   ├── __init__.py
│   │   │   └── operations.py
│   │   └── setup.py
│   └── pypy
│       └── pypy.py
├── poo
│   ├── clase_1
│   │   └── poo.py
│   ├── clase_2
│   │   └── poo.py
│   ├── clase_3
│   │   └── poo.py
│   └── clase_4
│       └── poo.py
├── tdd
│   └── clase_1
│       └── testing.py
├── tensorflow
│   ├── clase_1
│   │   └── clase_1.py
│   └── clase_2
│       └── tensorflow_datasets.ipynb
├── venv
├── LICENSE
└── README.md
```
