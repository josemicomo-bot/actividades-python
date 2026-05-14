# Actividad 17: Lista de diccionarios de ordenadores
# Objetivo: Registrar varios ordenadores con sus características en una lista de diccionarios

# Creamos una lista vacía donde guardaremos los diccionarios de ordenadores
ordenadores = []

# Usamos un bucle while que se repite indefinidamente (True siempre es verdadero)
while True:
    # Pedimos la marca del ordenador
    marca = input("Introduce la marca del ordenador (escribe 'fin' para terminar): ")
    
    # Si el usuario escribe "fin", salimos del bucle
    if marca.lower() == "fin":
        break
    
    # Pedimos el modelo del ordenador
    modelo = input("Introduce el modelo: ")
    
    # Pedimos la memoria RAM (convertimos a entero)
    memoria_ram = int(input("Introduce la memoria RAM (en GB): "))
    
    # Pedimos la capacidad del disco duro (convertimos a entero)
    capacidad_disco = int(input("Introduce la capacidad de disco (en GB): "))
    
    # Pedimos el sistema operativo
    sistema_operativo = input("Introduce el sistema operativo: ")
    
    # Creamos un diccionario con los datos del ordenador
    # Cada clave es el nombre de la característica y cada valor es lo que introdujo el usuario
    ordenador = {
        "marca": marca,
        "modelo": modelo,
        "memoria_ram": memoria_ram,
        "capacidad_disco": capacidad_disco,
        "sistema_operativo": sistema_operativo
    }
    
    # Añadimos el diccionario del ordenador a la lista
    ordenadores.append(ordenador)

# Mostramos un encabezado para la salida
print("\n=== Ordenadores registrados ===\n")

# Usamos un bucle for para recorrer cada ordenador de la lista
for ordenador in ordenadores:
    # Mostramos los datos de cada ordenador de forma legible
    print(f"Marca: {ordenador['marca']}")
    print(f"Modelo: {ordenador['modelo']}")
    print(f"Memoria RAM: {ordenador['memoria_ram']} GB")
    print(f"Capacidad de disco: {ordenador['capacidad_disco']} GB")
    print(f"Sistema operativo: {ordenador['sistema_operativo']}")
    # Dejamos una línea en blanco para separar ordenadores
    print()
