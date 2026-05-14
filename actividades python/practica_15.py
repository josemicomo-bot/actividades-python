# Actividad 15: Lista numerada de programas instalados
# Objetivo: Crear una lista con programas y mostrarla de forma numerada

# Creamos una lista con varios programas instalados en un ordenador
programas = [
    "Navegador",
    "Editor de texto",
    "Antivirus",
    "Reproductor multimedia",
    "Compresor de archivos"
]

# Mostramos un encabezado para la salida
print("=== Programas instalados ===\n")

# Usamos un bucle for con enumerate() para recorrer la lista
# enumerate() devuelve el índice (posición) y el elemento
# El índice comienza en 0, pero lo mostramos sumándole 1 para que comience en 1
for numero, programa in enumerate(programas, start=1):
    # Mostramos el número (posición) seguido del programa
    # start=1 hace que la numeración comience en 1 en lugar de 0
    print(f"{numero}. {programa}")
