n1 = float(input("Ingrese su primera nota: "))
n2 = float(input("Ingrese su primera nota: "))
n3 = float(input("Ingrese su primera nota: "))
n4 = float(input("Ingrese su primera nota: "))


if n1 == 0 or n2 == 0 or n3 == 0 or n4 == 0 or n1 > 7 or n2 > 7 or n3 > 7 or n4 > 7:
    print("Ingrese una nota desde el 2 hasta el 7")
else:
        promedio = (n1+n2+n3+n4)/4
        print(f"Su promedio es: {promedio:.1f}")


#PERIMETROOOOOOOO

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del triángulo es: {area:.2f}")
print(f"EL perímetro del triángulo es: {perimetro:.2f}")


num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))

suma = num1 + num2
resta = num1 - num2 
multiplicacion = num1 * num2 
division_decimales = num1/num2
division_entera = num1//num2
resto = num1 % num2
potencia = num1**num2

print("La suma de los dos numeros")