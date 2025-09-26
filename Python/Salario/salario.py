horas = float(input("¿Cuantas horas trabaja por semana?: "))
pago = float(input("¿Cuanto es su pago por hora trabajada?: "))

semanal = horas * pago
mensual = semanal * 4
ahorro = mensual * 0.10

print(f"Usted trabaja: {horas:.1f} horas semanalmente, ganando {pago:.1f} pesos por hora, resultando en un salario semanal de: {semanal:.1f} pesos y un salario mensual de {mensual:.1f} pesos. Siendo su ahorro final de {ahorro:.1f} pesos")