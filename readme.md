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

## Caso de Uso

Para este primer uso trabajemos con el modelo <a href="https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct">Qwen2.5-0.5B-Instruct</a>, el cual lo hostearemos de forma local gracias a la facilidad que nos ofrece el respositorio <a href="https://github.com/oobabooga/text-generation-webui"> text-generation-webui</a> donde podremos descargar de forma sencilla cualquier modelo que queramos usar y poder hacerle peticiones para que nos genere prompts.

Una vez iniciemos el programa `histories_generator.py` nos pedirá por consola información básica con la cual generará nuestra historia:

1. Tendremos el género de la historia:
   ```Python
   ¡Bienvenido al generador de historias!

   Elige el género de la historia (Si no se elige una de estas opciones, la opcion por defecto es "Aventura"):
   a) Fantasía
   b) Ciencia Ficción
   c) Terror
   d) Comedia
   e) Drama
   Selecciona una opción (a/b/c/d/e): b
   ```
   Aquí podemos ver los distintos géneros que podemos usar para nuestra historia, tendremos también una opción por defecto que será *Aventura* en el caso de que no usemos una de las opciones disponibles.

   Usaremos el género b - Ciencia Ficción en nuestro caso.

2. Deberemos elegir el nombre de nuestro personaje principal:
   ```Bash
   Nombre del personaje principal: Alice
   ```

3. Continuaremos por elegir el personaje secundario de nuestra historia:
   ```bash
   Nombre del personaje secundario: Bob
   ```

4. Seleccionaremos el lugar donde queramos que transcurra el relato: 
   ```bash
   Lugar donde transcurre el relato: Un bosque encantado
   ```

5. Lo que haremos a continuación es decidir una acción importante que se llevará a cabo:
   ```bash
   Acción importante que debe acontecer en la historia: Resolver un misterio
   ```

6. Por último, elegiremos el nivel de creatividad que queramos que tenga nuestra respuesta:
   ```bash
   Elige el nivel de creatividad:
   a) Creatividad alta
   b) Creatividad media
   c) Creatividad baja
   Selecciona una opción (a/b/c): b
   ``` 

   En nuestro caso lo dejaremos como creatividad media, que será la que dejaremos por defecto en caso de coger una opción distinta a las permitidas.
   ```bash
   Elige el nivel de creatividad:
   a) Creatividad alta
   b) Creatividad media
   c) Creatividad baja
   Selecciona una opción (a/b/c): f
   Opción no válida, se usará creatividad media por defecto.
   ```

Tras esto, tendremos el siguiente comentario mientras se genera nuestra respuesta:

```bash
Generando la historia... Esto puede tomar unos segundos.
```

Una vez finalize el programa podremos ver el siguiente mensaje devuelto:
```bash
=== Historia Generada ===
Alice y Bob caminaban por un bosque encantado cuando Alice se detuvo y dijo: "¡Esos árboles son extraños!"

Bob se acercó a Alice y dijo: "¿Sabes por qué? Están llenos de sombras que nunca cesan de moverse."

Alice asintió con la cabeza y dijo: "Eso es verdadero. Están moviéndose, pero no puedo ver a nadie detrás de ellos."

Bob se acercó más y dijo: "No, no hay nadie ahí. Solo sombras."

Alice y Bob siguieron su camino, pero Alice se preguntaba quién podría ser esa persona detrás de esas sombras.

Así comenzó la búsqueda de Alice y Bob por el bosque encantado, pero no tuvieron éxito en resolver el misterio de las sombras que nunca cesan de moverse. Alice y Bob se alejaron del bosque, pero la historia de los árboles y las sombras nunca se esfumó de su mente.

Finalmente, Alice y Bob encontraron una cueva en el bosque y descubrieron un libro de antiguos registros que contaba la historia de una antigua civilización que vivió en ese bosque. El libro decía que la sombra que nunca cesaba de moverse era el fantasma de una anciana que había muerto en la cueva.

Alice y Bob volvieron a caminar por el bosque, pero esta vez con una nueva perspectiva. Alice y Bob se sentían agradecidos por el misterio que había resuelto y la historia que había encontrado en el bosque encantado.

El final fue un sonido de alarma, pero Alice y Bob estaban a salvo. Alice y Bob habían resuelto un misterio

¿Quieres guardar la historia? (s/n)
```

Podremos ver que tendremos una opción al final del programa para guardar nuestra historia. 

Si le damos a que sí, creará una carpeta dentro del proyecto llamada *historias_generadas*, donde guardará nuestras historias en orden cardinal, de forma que nuestro documento guardado se llamará `historia_1.txt`.

Finalizará el programa mostrando:
```bash
La historia ha sido guardada en "historias_generadas\historia_1.txt".
```
