numeros = []
i= 1
suma = 0
print("Ingrese el 0 para terminar el programa")
print("Ingrese números: ")
while True:

    ingresar = int(input())
    if ingresar > 0:
        numeros.append(ingresar)
        suma = ingresar + suma
        i=i+1
    if ingresar == 0:
        break

promedio = suma/i
numeros.sort()
mayor = numeros[-1]
menor = numeros[0]
cantidad = len(numeros)

print(f"Promedio: {promedio}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
print(f"Cantidad de números ingresados: {cantidad}")
print(f"De mayor a menor: {numeros}")