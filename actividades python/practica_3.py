temperatura = int(input("Introduce la temperatura del procesador en grados: "))  # Pide la temperatura y la convierte a número entero

if 0 <= temperatura <= 110:  # Comprueba si la temperatura está entre 0 y 110 grados
    print("La temperatura es válida.")  # Si está en rango, muestra que es válida
else:  # Si no está en rango
    print("La temperatura no es válida. Debe estar entre 0 y 110 grados.")  # Muestra que no es válida
