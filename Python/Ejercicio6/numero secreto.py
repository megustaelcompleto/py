numero = 15
print("Adivine el número secreto:")
while True:
    respuesta=int(input(""))
    if respuesta > numero:
        print(f"El número secreto es menor a {respuesta}")
    elif respuesta < numero:
        print(f"El número secreto es mayor a {respuesta}")
    elif respuesta == numero:
        print("¡Correcto!")
        break