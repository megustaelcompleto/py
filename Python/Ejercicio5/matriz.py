matriz = [
    [5, 2, 9, 11],
    [4, 5, 6, 8],
    [7, 2, 9, 3]
    ]
print("Los números mayores a 5 son:")
for fila in matriz:
    for n in fila:
        if n > 5:
            print(n)
