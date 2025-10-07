dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
d = 0
i = 0
maximas = []
suma1 = 0
while True:
    print(f"Temperatura máxima del día {dias[d]}: ")
    maxima = int(input()) 
    maximas.append(maxima)
    match maxima:
        case n if n > 25:
            print("Temperatura alta")
        case n if 16 <= n <= 25:
            print("Temperatura templada")
        case n if n <= 15:
            print("Temperatura baja")
    print("")
    d +=1
    i +=1
    suma1 = suma1 + maxima
    if i >= 7:
        break

print("=================================================")
suma2 = 0
minimas = []
d = 0
i = 0
while True:
    print(f"Temperatura minima del día {dias[d]}")
    minima= int(input())
    minimas.append(minima)
    match minima:
        case n if n > 25:
            print("Temperatura alta")
        case n if 16 <= n <= 25:
            print("Temperatura templada")
        case n if n <= 15:
            print("Temperatura baja")
    suma2 = suma2 + minima
    d +=1
    i +=1
    if i >= 7:
        break

maximas.sort()
minimas.sort()
promedio1 = suma1/7
promedio2 = suma2/7
print(f"La temperatura más alta de la semana fue de {maximas[-1]}")
print(f"La temperatura más baja de la semana fue de {minimas[0]}")
print(f"El promedio de temperaturas altas fue de {promedio1}")
print(f"El promedio de temperaturas bajas fue de {promedio2}")


