contraseña_correcta = "1234"  
# Se establece la contraseña correcta
intentos = 0  
# Se inicializa el contador de intentos en 0
maximo_intentos = 3  
# Se establece el máximo de intentos permitidos

while intentos < maximo_intentos:  
    # Mientras el número de intentos sea menor que el máximo
    contraseña = input("Introduce la contraseña: ")  
    # Pide la contraseña al usuario
    intentos += 1  
    # Incrementa el contador de intentos en 1
    
    if contraseña == contraseña_correcta:  
        # Si la contraseña es correcta
        print("Acceso permitido.")  
        # Muestra acceso permitido
        break  
        # Sale del bucle
    elif intentos < maximo_intentos:  
        # Si no es correcta y quedan intentos
        print("Contraseña incorrecta. Te quedan", maximo_intentos - intentos, "intentos.")  
        # Muestra los intentos restantes
    else:  
        # Si se han agotado los intentos
        print("Acceso bloqueado. Has agotado los 3 intentos.")  
        # Muestra que el acceso está bloqueado
