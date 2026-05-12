espacio_libre = int(input("Introduce los GB libres del disco duro: "))  
# Pide los GB libres y los convierte a número entero

if espacio_libre >= 20:  
    # Si hay 20 GB o más libres
    print("Hay espacio suficiente en el disco.")  
    # Muestra que hay espacio suficiente
else:  
    # Si hay menos de 20 GB libres
    print("Conviene liberar espacio en el disco.")  
    # Recomienda liberar espacio
