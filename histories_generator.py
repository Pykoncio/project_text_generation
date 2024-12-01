import requests
import json
import os

# Configuración de la URL y cabeceras de la API
API_URL = "http://127.0.0.1:5000/v1/completions"
HEADERS = {"Content-Type": "application/json"}

def obtain_genre():
    """
    Obtiene el género sobre el cual se basará la historia generada.
    """
    print("\nElige el género de la historia (Si no se elige una de estas opciones, la opcion por defecto es \"Aventura\"):")
    print("a) Fantasía\nb) Ciencia Ficción\nc) Terror\nd) Comedia\ne) Drama")
    genre = input("Selecciona una opción (a/b/c/d/e): ").lower()
    if genre == "a":
        return "Fantasía"
    elif genre == "b":
        return "Ciencia Ficción"
    elif genre == "c":
        return "Terror"
    elif genre == "d":
        return "Comedia"
    elif genre == "e":
        return "Drama"
    else:
        print("Opción no válida, se usará el género \'Aventura\' por defecto.")
        return "Aventura"
    
def obtain_available_number(folder):
    """
    Devuelve el primer número disponible para el archivo en la carpeta dada.
    """
    existing_files = os.listdir(folder)
    
    # Extraer los números de los archivos (historia_n.txt)
    numbers = []
    for file in existing_files:
        if file.startswith("historia_") and file.endswith(".txt"):
            try:
                num = int(file.split("_")[1].split(".")[0])
                numbers.append(num)
            except ValueError:
                pass  

    numbers.sort()

    # Buscar el primer número faltante
    next_number = 1
    for num in numbers:
        if num != next_number:
            break
        next_number += 1
    
    return next_number
    
def save_history(history):
    """
    Guarda la historia en un archivo dentro de una carpeta del proyecto.
    Si la carpeta no existe, la crea.
    """
    folder = "historias_generadas"
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_count = obtain_available_number(folder)
    file_name = f"historia_{file_count}.txt"  
    full_path = os.path.join(folder, file_name)

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(history)

    print(f"\nLa historia ha sido guardada en \"{full_path}\".")

def obtain_parameters():
    """
    Solicita al usuario los datos necesarios para la historia y los parámetros de generación.
    """
    print("¡Bienvenido al generador de historias!")
    genre = obtain_genre()
    main_character = input("Nombre del personaje principal: ")
    secondary_character = input("Nombre del personaje secundario: ")
    place = input("Lugar donde transcurre el relato: ")
    important_action = input("Acción importante que debe acontecer en la historia: ")

    print("\nElige el nivel de creatividad:")
    print("a) Creatividad alta")
    print("b) Creatividad media")
    print("c) Creatividad baja")
    creativity = input("Selecciona una opción (a/b/c): ").lower()

    if creativity == "a":
        temperature = 1.0
    elif creativity == "b":
        temperature = 0.7
    elif creativity == "c":
        temperature = 0.3
    else:
        print("Opción no válida, se usará creatividad media por defecto.")
        temperature = 0.7

    return main_character, secondary_character, place, important_action, temperature, genre

def generate_history(main_character, secondary_character, place, important_action, temperature, genre):
    """
    Genera la historia mediante la API usando los datos proporcionados por el usuario.
    """
    max_tokens = 400
    prompt = (
        f"Escribe una historia emocionante de {genre}."
        f"Donde el personaje principal, {main_character}, "
        f"y el personaje secundario, {secondary_character}, se encuentren en {place}. "
        f"En esta historia, debe ocurrir lo siguiente: {important_action}. "
        f"La narrativa debe estar bien estructurada, ser interesante, limitada a {max_tokens - 50} tokens "
        f"y debe incluir un final claro y conciso de una frase."
        f"Proporciona únicamente la historia, sin introducción, explicaciones, ni comentarios adicionales."
    )

    body = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.9
    }

    try:
        response = requests.post(url=API_URL, headers=HEADERS, json=body)
        response.raise_for_status()
        message_response = json.loads(response.content.decode("utf-8"))
        history = message_response["choices"][0]["text"]
        return history.strip()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def main():
    """
    Función principal del programa.
    """
    main_character, secondary_character, place, important_action, temperature, genre = obtain_parameters()
    
    # Generar la historia
    print("\nGenerando la historia... Esto puede tomar unos segundos.\n")
    history = generate_history(main_character, secondary_character, place, important_action, temperature, genre)

    if history:
        print("=== Historia Generada ===")
        print(history)

        save = input("\n¿Quieres guardar la historia? (s/n)")
        if save.lower() == "s":
            save_history(history)
        else:
            print("¡Hasta la próxima!")
    else:
        print("No se pudo generar la historia. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
