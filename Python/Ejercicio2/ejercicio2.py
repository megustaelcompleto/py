nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
altura = float(input("Coloque su altura en metros: "))
peso = float(input("Coloque su peso en kilogramos: "))

imc = round(peso/(altura * altura), 2) # para redondear

if imc <= 18.4:
    print("Usted,",nombre,", está delgado y su IMC es:", imc)
else:
    if imc <= 25 and imc >= 18.5:
        print("Usted,",nombre,", está en un peso saludable y su IMC es:", imc)
    else:
        if imc > 25:
            print("Usted,",nombre,", está en sobrepeso y su IMC es:", imc)