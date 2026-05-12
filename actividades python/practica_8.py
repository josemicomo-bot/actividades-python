# Actividad 8. Comprobar usuario permitido

usuario_permitido = "admin"
usuario_introducido = input("Introduce tu nombre de usuario: ").strip()

if usuario_introducido == usuario_permitido:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")
