numeros = [4, -2, -5, 7, -1, 0, 6]
c=0
for i in numeros:
    if i < 0:
        c = i + c
        print(c)