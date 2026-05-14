def comprobar_nota(nota):
    if nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

nota = float(input("Introduce la nota: "))

resultado = comprobar_nota(nota)

print(resultado)