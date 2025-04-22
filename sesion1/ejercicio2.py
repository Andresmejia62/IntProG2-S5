#Control de inventario de un producto
cantidad_inicial = int(input("Ingresar la cantidad inicial en inventario"))
productos_recibidos = int(input("Ingresar la cantidad de productos recibidos"))
productos_vendidos = int(input("Ingresar la cantidad de productos vendidos"))

inventario_actual = (productos_recibidos + cantidad_inicial) - productos_vendidos
print(f""" El inventario inicial es = {cantidad_inicial}
Los productos recibidos son: {productos_recibidos}
Los productos vendidos son: {productos_vendidos}
El inventario final es: {inventario_actual}""")