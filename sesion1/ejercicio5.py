litros_consumidos_mes = float(input("Ingrese el total de litros consumidos en el mes: "))
cantidad_personas = int(input("Ingrese la cantidad de personas en la vivienda: "))
consumo_mensual_persona = litros_consumidos_mes / cantidad_personas
consumo_diario_persona = consumo_mensual_persona / 30
print(f"\nConsumo Total de Agua en el Mes: {litros_consumidos_mes} litros")
print(f"Cantidad de Personas en la Vivienda: {cantidad_personas}")
print(f"Consumo Mensual por Persona: {consumo_mensual_persona:.2f} litros")
print(f"Consumo Diario por Persona: {consumo_diario_persona:.2f} litros")
