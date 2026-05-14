# Actividad 14: Lista de periféricos
# Objetivo: Pedir 5 periféricos y guardarlos en una lista para mostrarlos después

# Creamos una lista vacía donde guardaremos los periféricos
perifericosó = []

# Usamos un bucle for para pedir 5 periféricos
# range(5) genera números: 0, 1, 2, 3, 4 (5 iteraciones)
for i in range(5):
    # Pedimos al usuario el nombre de un periférico
    # i+1 sirve para mostrar la posición empezando desde 1
    periferico = input(f"Introduce el periférico {i+1}: ")
    
    # Añadimos el periférico a la lista
    # append() añade el elemento al final de la lista
    perifericosó.append(periferico)

# Mostramos un encabezado para la salida
print("\n=== Periféricos introducidos ===")

# Usamos un bucle for para recorrer cada periférico de la lista
# Se ejecuta una vez por cada elemento en la lista
for periferico in perifericosó:
    # Mostramos cada periférico en una línea diferente
    print(periferico)
