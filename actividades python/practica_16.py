# Actividad 16: Contar incidencias informáticas
# Objetivo: Pedir incidencias hasta que el usuario escriba "fin" y contar cuántas hay

# Inicializamos un contador en 0
# Este contador aumentará cada vez que el usuario introduzca una incidencia
contador = 0

# Creamos un bucle while que se repite mientras la condición sea verdadera
# La condición se mantendrá verdadera hasta que el usuario escriba "fin"
while True:
    # Pedimos al usuario que introduzca una incidencia
    incidencia = input("Introduce una incidencia informática (escribe 'fin' para terminar): ")
    
    # Comprobamos si el usuario escribió "fin"
    # Si es así, salimos del bucle
    if incidencia.lower() == "fin":
        # break detiene el bucle inmediatamente
        break
    
    # Si no escribió "fin", sumamos 1 al contador
    # Esto significa que se registró una incidencia
    contador += 1

# Después de terminar el bucle, mostramos el número total de incidencias registradas
print(f"\nTotal de incidencias registradas: {contador}")
