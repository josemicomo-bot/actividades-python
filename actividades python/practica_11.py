# Actividad 11: Cuenta atrás de inicio del sistema
# Objetivo: Mostrar una cuenta atrás desde 10 hasta 1 y luego un mensaje de inicio

# Usamos un bucle for que recorre los números desde 10 hasta 1 (descendente)
# range(10, 0, -1) genera números: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# El tercer parámetro (-1) indica que vamos hacia atrás
for numero in range(10, 0, -1):
    # Mostramos cada número en la pantalla
    print(numero)

# Después de terminar el bucle, mostramos el mensaje de inicio del sistema
print("Inicio del sistema")
