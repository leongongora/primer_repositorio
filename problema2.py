import string

def contar_frecuencia_palabras(lista_palabras: list[str], ruta_fichero: str) -> dict[str, int]:
    
    #Cuenta cuántas veces aparecen las palabras de una lista en un fichero de texto.
    
    
    frecuencias = {palabra.lower(): 0 for palabra in lista_palabras}

    try:
        with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()
    except FileNotFoundError:
        print(f"Error: El fichero en la ruta '{ruta_fichero}' no fue encontrado.")
        return {}
#se verifica que exista el fichero
    traductor = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    contenido_limpio = contenido.lower().translate(traductor)
    #elimina signos de puntuación y convierte a minúsculas
    
    for palabra_fichero in contenido_limpio.split():
        if palabra_fichero in frecuencias:
            frecuencias[palabra_fichero] += 1
    
    return frecuencias

#programa de prueba

ruta_fichero_existente = "texto_ejemplo.txt"
palabras_a_buscar = ["inteligencia", "artificial", "aprendizaje", "actual", "espacial", "y", "una", "película"]
#lista de palabras a buscar

resultado_frecuencias = contar_frecuencia_palabras(palabras_a_buscar, ruta_fichero_existente)
print("\n--- Frecuencia de palabras ---")
if resultado_frecuencias:
    #para imprimir el resultado se crea una lista con palabras clave del cdiccionario ordenadas y se itera sobre ella
    for palabra in sorted(resultado_frecuencias.keys()):
        frecuencia = resultado_frecuencias[palabra]
        print(f"- '{palabra}': {frecuencia} veces")
else:
    print("No se encontraron resultados o hubo un error al leer el fichero.")
