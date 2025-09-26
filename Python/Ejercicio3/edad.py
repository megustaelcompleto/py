edad = int(input("Edad: "))

if edad == 0:
    print("Ingrese edad válida")
else:
    if edad > 64:
        print("Usted es anciano")
    elif edad >= 18:
        print("Usted es adulto")
    elif edad >= 13:
        print("Usted es un adolescente")
    elif edad >= 1:
        print("Usted es un niño")
