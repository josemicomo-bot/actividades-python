memoria_ram = int(input("Introduce la cantidad de memoria RAM en GB: "))  # Pide la cantidad de RAM y la convierte a número entero

if memoria_ram < 8:  # Si la RAM es menor de 8 GB
    print("Memoria RAM baja.")  # Se clasifica como baja
elif memoria_ram <= 15:  # Si la RAM está entre 8 y 15 GB
    print("Memoria RAM media.")  # Se clasifica como media
else:  # Si la RAM es 16 GB o más
    print("Memoria RAM alta.")  # Se clasifica como alta
