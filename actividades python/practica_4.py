# Actividad 4. Clasificar temperatura del procesador

temperatura = int(input("Introduce la temperatura del procesador en grados: "))

if temperatura < 60:
    print("Temperatura normal.")
elif temperatura <= 85:
    print("Temperatura alta.")
else:
    print("Temperatura peligrosa.")
