# Actividad 6. Clasificar memoria RAM

memoria_ram = int(input("Introduce la cantidad de memoria RAM en GB: "))

if memoria_ram < 8:
    print("Memoria RAM baja.")
elif memoria_ram <= 15:
    print("Memoria RAM media.")
else:
    print("Memoria RAM alta.")
