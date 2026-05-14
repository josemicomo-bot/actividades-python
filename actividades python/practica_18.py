# Actividad 18: Función para calcular el precio con IVA
# Objetivo: Crear una función que añada IVA a un precio y mostrar el resultado

# Definimos una función que recibe un precio como parámetro
# def introduce la definición de una función
# calcular_precio_con_iva es el nombre de la función
# precio es el parámetro que la función recibirá
def calcular_precio_con_iva(precio):
    # Definimos el IVA como 21% (0.21 en formato decimal)
    iva = 0.21
    
    # Calculamos el precio final multiplicando el precio por (1 + IVA)
    # Esto equivale a: precio + (precio * 0.21)
    precio_final = precio * (1 + iva)
    
    # return devuelve el resultado de la función al programa que la llamó
    return precio_final

# Pedimos al usuario el precio del producto
# float() convierte el texto a número decimal
precio_producto = float(input("Introduce el precio del producto: "))

# Llamamos a la función y pasamos el precio como parámetro
# La función calcula el precio con IVA y lo devuelve
precio_con_iva = calcular_precio_con_iva(precio_producto)

# Mostramos el resultado final
# f-string permite insertar variables dentro de la cadena usando {variable}
print(f"Precio original: {precio_producto}€")
print(f"Precio con IVA (21%): {precio_con_iva:.2f}€")
