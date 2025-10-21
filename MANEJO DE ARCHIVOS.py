# EJERCICIO 1
productos = [
    "lapicera, 120.5, 30\n",
    "cuaderno, 250.0, 50\n",
    "regla, 100.0, 20\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

print("Archivo 'productos.txt' creado con éxito.")

# EJERCICIO 2

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        # Convierte la primera letra del nombre en mayúscula
        nombre = partes[0].capitalize()
        precio = partes[1]
        cantidad = partes[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# EJERCICIO 3
print("\nIngrese un nuevo producto:")

nuevo_nombre = input("Nombre: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")

nueva_linea = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(nueva_linea)

print("\nProducto agregado con éxito al archivo.")
