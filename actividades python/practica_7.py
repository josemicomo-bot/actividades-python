# Actividad 7. Menú de mantenimiento básico

print("=== MENÚ DE MANTENIMIENTO ===")
print("1. Comprobar disco")
print("2. Comprobar memoria RAM")
print("3. Comprobar temperatura")
print("4. Salir")

opcion = input("Elige una opción (1-4): ")

if opcion == "1":
    print("Comprobando disco...")
elif opcion == "2":
    print("Comprobando memoria RAM...")
elif opcion == "3":
    print("Comprobando temperatura...")
elif opcion == "4":
    print("Saliendo del programa...")
else:
    print("Opción no válida.")
