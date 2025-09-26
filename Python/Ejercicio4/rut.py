run = input("Ingrese su RUN: ")

dv = str(run[-1])


dv = str(run[-1])

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
    print("Su RUN es correcto")
    if str(digito_resta) == str(10):
        if dv == "k":
            print("Su RUN es valido")
        else:
            if str(digito_resta) == str(11):
                if dv == 0:
                    print("Su RUN es valido")
                else:
                    print("Su RUN es invalido")
            else:
                print("Su RUN es invalido")
    else:
        print("Su RUN es invalido")
else:
    print("Su RUN es inválido")
        



#falta provisorio