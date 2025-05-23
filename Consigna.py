# Gestión de Ventas de Productos con Lista y Matriz

from FuncionesConsigna import menu
# Datos iniciales
productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70],  # Producto A
    [80, 55, 45],  # Producto B
    [40, 65, 75]   # Producto C
]

"""
for i in range(len(ventas)):
    num = 1
    for j in range(len(ventas)):
        ventas[i][j] = int(input(f"Ingresa las ventas de {productos[i]} en el Trimestre {num}: "))
        num += 1
"""

# Iniciar el programa
menu(productos, ventas)
