# Actividad 13: Suma de consumos eléctricos
# Objetivo: Registrar componentes de un ordenador y calcular el consumo total

# Creamos un diccionario vacío donde guardaremos los componentes y su consumo
componentes = {}

# Usamos un bucle for para pedir 5 componentes
# range(5) genera números: 0, 1, 2, 3, 4 (5 iteraciones)
for i in range(5):
    # Pedimos el nombre del componente al usuario
    nombre = input(f"Introduce el nombre del componente {i+1}: ")
    
    # Pedimos el consumo en vatios del componente
    # float() convierte el texto a número decimal
    consumo = float(input(f"Introduce el consumo en vatios del componente {i+1}: "))
    
    # Añadimos el componente al diccionario
    # La clave es el nombre y el valor es el consumo
    componentes[nombre] = consumo

# Mostramos un encabezado para la salida
print("\n=== Componentes registrados ===")

# Usamos un bucle for para recorrer cada componente del diccionario
# .items() devuelve pares (clave, valor)
for nombre, consumo in componentes.items():
    # Mostramos el nombre del componente y su consumo
    print(f"{nombre}: {consumo} vatios")

# Usamos sum() para sumar todos los valores del diccionario
# .values() devuelve solo los valores (no las claves)
# Esto nos da el consumo total
consumo_total = sum(componentes.values())

# Mostramos el consumo total del equipo
print(f"\nConsumo total del equipo: {consumo_total} vatios")
