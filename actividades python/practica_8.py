usuario_permitido = "admin"  # Se establece el usuario permitido
usuario_introducido = input("Introduce tu nombre de usuario: ").strip()  # Pide el usuario y elimina espacios en blanco al inicio y final

if usuario_introducido == usuario_permitido:  # Si el usuario introducido es igual al permitido
    print("Acceso permitido.")  # Muestra acceso permitido
else:  # Si el usuario no coincide
    print("Acceso denegado.")  # Muestra acceso denegado
