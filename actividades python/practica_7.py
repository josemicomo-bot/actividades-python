print("=== MENÚ DE MANTENIMIENTO ===")  # Muestra el título del menú
print("1. Comprobar disco")  # Opción 1
print("2. Comprobar memoria RAM")  # Opción 2
print("3. Comprobar temperatura")  # Opción 3
print("4. Salir")  # Opción 4

opcion = input("Elige una opción (1-4): ")  # Pide al usuario que elija una opción

if opcion == "1":  # Si elige la opción 1
    print("Comprobando disco...")  # Muestra mensaje de comprobación de disco
elif opcion == "2":  # Si elige la opción 2
    print("Comprobando memoria RAM...")  # Muestra mensaje de comprobación de RAM
elif opcion == "3":  # Si elige la opción 3
    print("Comprobando temperatura...")  # Muestra mensaje de comprobación de temperatura
elif opcion == "4":  # Si elige la opción 4
    print("Saliendo del programa...")  # Muestra mensaje de salida
else:  # Si elige una opción no válida
    print("Opción no válida.")  # Muestra que la opción no es válida
