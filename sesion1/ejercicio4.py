distancia_recorrida = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
precio_por_litro = float(input("Ingrese el precio por litro de combustible: "))
rendimiento = distancia_recorrida / litros_consumidos
gasto_total = litros_consumidos * precio_por_litro
print(f"\nDistancia Recorrida: {distancia_recorrida} km")
print(f"Litros Consumidos: {litros_consumidos} litros")
print(f"Precio por Litro: {precio_por_litro} unidades monetarias")
print(f"Rendimiento del Vehículo: {rendimiento:.2f} km/l")
print(f"Gasto Total en Combustible: {gasto_total:.2f} unidades monetarias")
