maximas = []
minimas = []
i=1
c=1
print("Ingrese temperaturas máximas: ")

while True:
    temperatura_max = int(input())
    maximas.append(temperatura_max)
    i=i+1
    match temperatura_max:
        case > 25:
            print("Alta")
        case < 16:
    if i >= 7:
        print("Ingrese temperaturas mínimas: ")
        while True:
            temp_min = float(input)
            minimas.append(temp_min)
            c=c+1




