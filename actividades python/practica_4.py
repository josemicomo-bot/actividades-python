temperatura = int(input("Introduce la temperatura del procesador en grados: "))  # Pide la temperatura y la convierte a número entero

if temperatura < 60:  # Si la temperatura es menor de 60 grados
    print("Temperatura normal.")  # Se considera normal
elif temperatura <= 85:  # Si la temperatura es entre 60 y 85 grados
    print("Temperatura alta.")  # Se considera alta
else:  # Si la temperatura es mayor de 85 grados
    print("Temperatura peligrosa.")  # Se considera peligrosa
