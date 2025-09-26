nombre = input("Escriba su nombre: ")
curso = input("Ingrese su Curso: ")
n1 = float(input("Ingrese su la primera nota: "))
n2 = float(input("Ingrese su la segunda nota: "))
n3 = float(input("Ingrese su la tercera nota: "))
n4 = float(input("Ingrese su la cuarta nota: "))

promedio = (n1+n2+n3+n4)/4

if ( 2 <= n1 <= 7 and 2 <= n2 <= 7 and 2 <= n3 <= 7 and 2 <= n4 <= 7):
    if promedio >= 4:
        print(f"El estudiante {nombre} de {curso} es promovido con promedio final {promedio:.1f}")
    else:
        if promedio < 4:
            examen = float(input("Ingrese una nota de examen: "))
            promedio2 = (examen + promedio)/2
            if ( 2 <= examen <= 7):
                if promedio2 >= 4:
                    print(f"El estudiante {nombre} del curso {curso} es promovido con promedio final {promedio2:.1f}")
                else:
                    print(f"El estudiante {nombre} del curso {curso} es reprobado con promedio final {promedio2:.1f}")
            else:
                print("Ingrese una nota válida, intente de nuevo")
else:
    print("Ingrese notas desde la nota 2 hasta la nota 7")
