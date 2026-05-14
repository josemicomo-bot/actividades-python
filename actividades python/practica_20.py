# Actividad 20: Saludo personalizado con control de errores
# Objetivo: Pedir nombre y saludar, validando que no esté vacío

# Definimos una función que recibe el nombre como parámetro
# def introduce la definición de una función
# saludar_alumno es el nombre de la función
# nombre es el parámetro que recibirá
def saludar_alumno(nombre):
    # print() muestra texto en la pantalla
    # f-string permite insertar la variable nombre dentro de la cadena
    print(f"Hola {nombre}, bienvenido al programa de prácticas de Python")
    print("Esperamos que disfrutes aprendiendo sobre administración de sistemas")

# Inicializamos la variable nombre como vacía
# Esto nos permite entrar al bucle while
nombre = ""

# Usamos un bucle while que se repite mientras el nombre esté vacío
# Este bucle fuerza al usuario a introducir un nombre válido
while nombre == "":
    # Pedimos al usuario que introduzca su nombre
    nombre = input("Introduce tu nombre: ")
    
    # Usamos strip() para eliminar espacios al principio y final
    # Esto evita que el usuario introduzca solo espacios en blanco
    nombre = nombre.strip()
    
    # Comprobamos si el nombre sigue estando vacío
    if nombre == "":
        # Mostramos un mensaje de error si está vacío
        print("Error: debes introducir un nombre válido\n")

# Si llegamos aquí, el nombre es válido, así que llamamos a la función
# Pasamos el nombre como parámetro
saludar_alumno(nombre)
