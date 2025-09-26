run = input("Ingrese su RUN: ")

dv = str(run[-1])

if len(run) == 10:
    n1 = int(run[0]) * 3
    n2 = int(run[1]) * 2
    n3 = int(run[2]) * 7
    n4 = int(run[3]) * 6
    n5 = int(run[4]) * 5
    n6 = int(run[5]) * 4
    n7 = int(run[6]) * 3
    n8 = int(run[7]) * 2

    suma = n1+n2+n3+n4+n5+n6+n7+n8 
    division = suma / 11
    resto = suma % 11
    digito_resta = 11 - resto

    print("DV:", dv) 
    print(n1, n2, n3, n4, n5, n6, n7, n8) 
    print(suma) 
    print(division) 
    print(resto) 
    print(digito_resta) 


    if str(digito_resta) == dv:
        print("Su RUN está correcto")
    elif str(digito_resta) == str(10) and dv == "k":
            print("Su RUN está correcto")
    elif str(digito_resta) == str(11) and dv == str(0):
                print("Su RUN está correcto")
    else:
                print("RUN inválido")
                
elif len(run) == 11:
    n0 = int(run[0]) * 4
    n1 = int(run[1]) * 3
    n2 = int(run[2]) * 2
    n3 = int(run[3]) * 7
    n4 = int(run[4]) * 6
    n5 = int(run[5]) * 5
    n6 = int(run[6]) * 4
    n7 = int(run[7]) * 3
    n8 = int(run[8]) * 2


    suma = n0+n1+n2+n3+n4+n5+n6+n7+n8 
    division = suma / 11
    resto = suma % 11
    digito_resta = 11 - resto

    print("DV:", dv) 
    print(n0+n1, n2, n3, n4, n5, n6, n7, n8) 
    print(suma) 
    print(division) 
    print(resto) 
    print(digito_resta) 


    if str(digito_resta) == dv:
        print("Su RUN está correcto")
    elif str(digito_resta) == str(10) and dv == "k":
            print("Su RUN está correcto")
    elif str(digito_resta) == str(11) and dv == str(0):
                print("Su RUN está correcto")
    else:
                print("RUN inválido")






