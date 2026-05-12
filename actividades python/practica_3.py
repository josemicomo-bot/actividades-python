# Actividad 3. Comprobar temperatura válida

temperatura = int(input("Introduce la temperatura del procesador en grados: "))

if 0 <= temperatura <= 110:
    print("La temperatura es válida.")
else:
    print("La temperatura no es válida. Debe estar entre 0 y 110 grados.")
