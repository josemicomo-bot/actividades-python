numero = int(input("Introduce un numero: "))

for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print (f"{numero} * {multiplicador} = {resultado}")