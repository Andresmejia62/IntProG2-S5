capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
años = int(input("Ingrese la cantidad de años: "))
tasa_decimal = tasa_interes / 100
valor = (1 + tasa_decimal) ** años
monto_final = capital_inicial * valor
interes_ganado = monto_final - capital_inicial
print(f"\nCapital Inicial: {capital_inicial}")
print(f"Tasa de Interés Anual: {tasa_interes}%")
print(f"Años: {años}")
print(f"Monto Final: {monto_final:.2f}")
print(f"Interés Ganado: {interes_ganado:.2f}")
