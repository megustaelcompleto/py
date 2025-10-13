while True:
    run = int(input("Ingrese su RUN: "))
    if run == 0:
        break
    dv = input("Digito verificador: ")

    multi = 2
    suma = 0

    for i in reversed(str(run)):
        valor = int(i) * multi
        suma = suma + valor
        multi = multi + 1
        if multi == 8:
            multi = 2
        

    resto = suma%11
    digito = 11 - resto


    print("El digito verificador es: ", digito)

    if str(digito) == dv:
        print("RUN correcto")
    elif str(digito) == str(10) and dv == "k":
            print("RUN correcto")
    elif str(digito) == str(11) and dv == str(0):
                print("RUN correcto")
    else:
                print("Digito verificador inválido")
    

