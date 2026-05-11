suma = 0

numero = int(input("Introduce un número, 0 para terminar: "))

while numero != 0:
    suma += numero
    numero = int(input("Introduce un número, 0 para terminar: "))

print("La suma de los números es:", {suma})
