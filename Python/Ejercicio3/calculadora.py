n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

"1 = SUMA. 2 = RESTA. 3 = MULTIPLICACIÓN. 4 = DIVISIÓN"

operacion = int(input("Ingrese la operación deseada: "))

if ( 1 <= operacion <= 4):
    if operacion == 1:
        print("El resultado es: ", (n1 + n2))

    if operacion == 2:
        print("El resultado es: ", (n1 - n2))

    if operacion == 3:
        print("El resultado es: ", (n1 * n2))

    if operacion == 4 and n2 == 0:
        print("No se puede divir por cero, ingrese otro número")
    else:
        print("El resultado es: ", (n1//n2))
else:
    print("Ingrese uno de estos números: 1,2,3,4")
