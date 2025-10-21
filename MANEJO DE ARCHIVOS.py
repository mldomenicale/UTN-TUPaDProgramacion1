# EJERCICIO 1
productos = [
    "lapicera,120.5,30\n",
    "cuaderno,250.0,50\n",
    "regla,100.0,20\n"
]
with open("productos.txt", "w") as archivo:
    archivo.write("Nombre,Precio,Cantidad\n")
    archivo.writelines(productos)

print("Archivo 'productos.txt' creado con éxito.")

# EJERCICIO 2

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        nombre = partes[0].title()
        precio = float(partes[1])
        cantidad = int(partes[2])
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# EJERCICIO 3
while True:
    print("\nIngrese un nuevo producto:")
    nuevo_nombre = input("Nombre: ").strip().title()

    while True:
        try:
            nuevo_precio = float(input("Precio: "))
            nueva_cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("Error: ingrese un número válido para precio y cantidad.")

    nueva_linea = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

    with open("productos.txt", "a") as archivo:
        archivo.write(nueva_linea)

    continuar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\nProductos agregados con éxito al archivo.")

# EJERCICIO 4
productos = []

with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        partes = linea.strip().split(",")
        producto = {
            "nombre": partes[0].title(),
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)

for i, p in enumerate(productos, start=1):
    print(
        f"{i}. {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# EJERCICIO 5
nombre_buscar = input(
    "Ingrese el nombre del producto a buscar: ").strip().title()

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(
            f"Producto encontrado:\nNombre: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print(f"Error: El producto '{nombre_buscar}' no existe en la lista.")


# EJERCICIO 6

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("Archivo 'productos.txt' actualizado correctamente.")
