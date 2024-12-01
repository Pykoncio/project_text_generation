# Generador de Historias con LLM

Este proyecto es un programa en Python que genera historias personalizadas utilizando la API de Generation Text WebUI. El usuario proporciona los datos clave y ajusta parámetros como la creatividad para obtener narrativas únicas.

Puedes emplear este proyecto como base para realizar implementaciones en tus propias aplicaciones, tan solo debes reemplazar la url donde hacemos la petición por la api del modelo **LLM** que vayas a usar.

## Características
- Solicita datos clave como el género, personajes, lugar y acciones importantes.
- Permite elegir el nivel de creatividad de la narrativa.
- Genera historias dinámicas mediante una API compatible con modelos LLM.

## Requisitos
- Python 3.x

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/histories_generator.git
   ```

2. Hay dos opciones para instalar o usar las dependencias necesarias para el proyecto:

   2.1. Instala las dependencias desde el archivo `requeriments.txt`:
    ```bash
   pip install -r requirements.txt
   ```

   2.2. Utiliza la `Virtual Environment` de *python* para no dejar instalaciones residuales en tu equipo (**Opción recomendada**). Para ello ejecuta el siguiente comando en la terminal desde el fichero del proyecto:

   ```bash
   .\myenv\Scripts\activate
   ```

   - Cuando quieras abandonar la *virtual environment* utiliza el siguiente comando:
      ```bash
      deactivate
      ```



3. Ejecuta el programa con:
    ```bash
    python histories_generator.py
    ```

## Uso

Una vez iniciemos el programa `histories_generator.py` nos pedirá por consola información básica con la cual generará nuestra historia.


