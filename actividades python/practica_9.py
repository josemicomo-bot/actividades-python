# Actividad 9. Intentos de acceso con contraseña

contraseña_correcta = "1234"
intentos = 0
maximo_intentos = 3

while intentos < maximo_intentos:
    contraseña = input("Introduce la contraseña: ")
    intentos += 1
    
    if contraseña == contraseña_correcta:
        print("Acceso permitido.")
        break
    elif intentos < maximo_intentos:
        print(f"Contraseña incorrecta. Te quedan {maximo_intentos - intentos} intentos.")
    else:
        print("Acceso bloqueado. Has agotado los 3 intentos.")
