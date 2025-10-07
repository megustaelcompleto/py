votos = [0, 0, 0]

print("=== VOTACIÓN PRESIDENTE DE LA REPÚBLICA DE CHILE===")
print("1. El malo")
print("2. Quiere plata")
print("3. El bueno")
print("0. Terminar votación")
a = 0
b = 0
c = 0
while True:
    voto = int(input("Vote: "))

    match voto:
        case 1:
            a = 1 + a
            votos[0] = a
        case 2:
            b = 1 + b
            votos[1] = b
        case 3:
            c = 1 + c
            votos[2] = c
        case 0:
            break
        case _:
            break

print(f"El candidato número 1 recibió: {votos[0]} votos")
print(f"El candidato número 2 recibió: {votos[1]} votos")
print(f"El candidato número 3 recibió: {votos[2]} votos")