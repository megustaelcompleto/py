
print("1: Suma    2: Resta    3: Multiplicación    4: División")
print("Escriba salir para terminar el programa")
while True:
    operacion=input("Ingrese su operación o termine el programa: ")
    if str(operacion.lower()) == "salir":
        break
    else:
        n1=int(input("Número 1: "))
        n2=int(input("Número 2: "))
        if operacion == str(1):
            print(n1+n2)
        elif operacion == str(2):
            print(n1-n2)
        elif operacion == str(3):
            print(n1*n2)
        elif operacion == str(4):
            print(n1/n2)

