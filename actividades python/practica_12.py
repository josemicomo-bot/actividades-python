# Actividad 12: Conversión de GB a MB
# Objetivo: Pedir una cantidad en GB y convertirla a MB

# Pedimos al usuario que introduzca una cantidad en GB
# input() lee lo que escribe el usuario como texto
# float() convierte ese texto a número decimal para poder hacer cálculos
gb = float(input("Introduce una cantidad en GB: "))

# Realizamos la conversión: 1 GB = 1024 MB
# Multiplicamos los GB por 1024 para obtener MB
mb = gb * 1024

# Mostramos el resultado de la conversión
# f-string permite insertar variables dentro de la cadena usando {variable}
print(f"{gb} GB equivalen a {mb} MB")
