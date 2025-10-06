i = 1
notas = []
suma = 0
asignatura = input("Asignatura: ")
while True:
    nota = float(input(f"Ingrese nota {i}: "))
    notas.append(nota)
    suma = nota + suma
    if i >= 5:
        break
    i = i + 1

print(f"Las notas de {asignatura.upper()} son: ")
for c in notas:
    print(c)
promedio = suma/i
print(f"Promedio final: {promedio}")

if promedio < 4:
    print("Reprobado")
else:
    print("Aprobado")