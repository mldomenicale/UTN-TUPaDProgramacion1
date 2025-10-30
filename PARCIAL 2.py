import csv
import os

# funciones de ayuda


def normalizar_titulo(titulo):
    # saco espacios extras y paso todo a minúscula para comparar bien los títulos
    return " ".join(titulo.split()).lower()


def es_entero_no_negativo(texto):
    # verifico que sea un número entero >= 0
    return texto.isdigit()


# cargar y guardar catálogo
def cargar_catalogo(nombre_archivo):
    # leo el CSV si existe, si no devuelvo lista vacía
    catalogo = []
    with open(nombre_archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            titulo = fila.get("TITULO", "").strip()
            cantidad = fila.get("CANTIDAD", "").strip()
            # agrego solo si título y cantidad son válidos
            if titulo != "" and es_entero_no_negativo(cantidad):
                catalogo.append({"TITULO": titulo, "CANTIDAD": int(cantidad)})
    return catalogo


def guardar_catalogo(nombre_archivo, catalogo):
    # guardo todo el catálogo en el CSV
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow(
                {"TITULO": libro["TITULO"], "CANTIDAD": libro["CANTIDAD"]})


# funciones de búsqueda
def buscar_indice_por_titulo(catalogo, titulo_buscar):
    # busco el índice del libro por título, devuelvo -1 si no existe
    objetivo = normalizar_titulo(titulo_buscar)
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro["TITULO"]) == objetivo:
            return i
    return -1


# mostrar catálogo
def mostrar_catalogo(catalogo):
    # muestro todos los libros con su cantidad
    print("\n--- Catálogo de la Biblioteca ---")
    if not catalogo:
        print("No hay libros cargados")
        return
    print(f"{'TÍTULO'} | {'CANTIDAD'}")
    for libro in catalogo:
        print(f"{libro['TITULO']} | {libro['CANTIDAD']}")
    print()


# funciones del menú
def ingresar_titulos_multiples(catalogo, nombre_archivo):
    # cargar varios libros a la vez
    cant_texto = input("¿Cuántos libros quiere cargar? ").strip()
    if not es_entero_no_negativo(cant_texto) or int(cant_texto) <= 0:
        print("Tiene que ser un número entero positivo")
        return
    cantidad = int(cant_texto)
    agregados = 0
    for n in range(1, cantidad+1):
        print(f"\nLibro {n} de {cantidad}")
        while True:
            titulo = input("Título: ").strip()
            if titulo == "":
                print("No puede estar vacío el título")
                continue
            if buscar_indice_por_titulo(catalogo, titulo) != -1:
                print("Ese título ya existe, poné otro")
                continue
            break
        while True:
            cant_inicial = input("Cantidad inicial (>=0): ").strip()
            if not es_entero_no_negativo(cant_inicial):
                print("Cantidad inválida, tiene que ser entero >=0")
                continue
            break
        catalogo.append({"TITULO": " ".join(titulo.split()),
                        "CANTIDAD": int(cant_inicial)})
        agregados += 1
    if agregados > 0:
        guardar_catalogo(nombre_archivo, catalogo)
        print(f"Se agregaron {agregados} libros y guardé el catálogo")


def ingresar_ejemplares(catalogo, nombre_archivo):
    # sumo cantidad a un libro ya existente
    titulo = input("Título a actualizar: ").strip()
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print("Ese título no existe")
        return
    cant_sumar = input("Cantidad a sumar (>0): ").strip()
    if not es_entero_no_negativo(cant_sumar) or int(cant_sumar) <= 0:
        print("Debe ser entero positivo")
        return
    catalogo[idx]["CANTIDAD"] += int(cant_sumar)
    guardar_catalogo(nombre_archivo, catalogo)
    print(
        f"Se sumaron {cant_sumar} ejemplares a '{catalogo[idx]['TITULO']}'. Nuevo stock: {catalogo[idx]['CANTIDAD']}")


def consultar_disponibilidad(catalogo):
    # busco un libro y digo cuantos ejemplares hay
    titulo = input("Título a consultar: ").strip()
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print("Ese título no existe")
        return
    print(
        f"'{catalogo[idx]['TITULO']}' tiene {catalogo[idx]['CANTIDAD']} ejemplares")


def listar_agotados(catalogo):
    # muestro solo los libros con cantidad 0
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    if not agotados:
        print("No hay libros agotados")
        return
    print("\nLibros agotados:")
    for libro in agotados:
        print(f"- {libro['TITULO']}")


def agregar_titulo_individual(catalogo, nombre_archivo):
    # agrego un libro individual
    while True:
        titulo = input("Título: ").strip()
        if titulo == "":
            print("No puede estar vacío")
            continue
        if buscar_indice_por_titulo(catalogo, titulo) != -1:
            print("Ese título ya existe, poné otro")
            continue
        break
    while True:
        cant_inicial = input("Cantidad inicial (>=0): ").strip()
        if not es_entero_no_negativo(cant_inicial):
            print("Cantidad inválida")
            continue
        break
    catalogo.append({"TITULO": " ".join(titulo.split()),
                    "CANTIDAD": int(cant_inicial)})
    guardar_catalogo(nombre_archivo, catalogo)
    print(f"Se agregó '{titulo}' con {cant_inicial} ejemplares")


def actualizar_ejemplares_prestamo_devolucion(catalogo, nombre_archivo):
    # prestamo o devolucion de 1 ejemplar
    titulo = input("Título: ").strip()
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print("Ese título no existe")
        return
    print("1. Préstamo")
    print("2. Devolución")
    opcion = input("Elija 1 o 2: ").strip()
    match opcion:
        case "1":
            if catalogo[idx]["CANTIDAD"] <= 0:
                print("No se puede prestar, no hay ejemplares")
                return
            catalogo[idx]["CANTIDAD"] -= 1
            guardar_catalogo(nombre_archivo, catalogo)
            print(
                f"Préstamo realizado. Nuevo stock: {catalogo[idx]['CANTIDAD']}")
        case "2":
            catalogo[idx]["CANTIDAD"] += 1
            guardar_catalogo(nombre_archivo, catalogo)
            print(
                f"Devolución realizada. Nuevo stock: {catalogo[idx]['CANTIDAD']}")
        case _:
            print("Opción inválida")


# menú principal
def mostrar_menu():
    print("\n" + "*"*40)
    print("1. Ingresar títulos múltiples")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título individual")
    print("7. Actualizar ejemplares (Préstamo/Devolución)")
    print("8. Salir")
    print("*"*40)


def main():
    # acá empieza todo
    nombre_archivo = "catalogo.csv"
    catalogo = cargar_catalogo(nombre_archivo)

    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        match opcion:
            case "1":
                ingresar_titulos_multiples(catalogo, nombre_archivo)
            case "2":
                ingresar_ejemplares(catalogo, nombre_archivo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                agregar_titulo_individual(catalogo, nombre_archivo)
            case "7":
                actualizar_ejemplares_prestamo_devolucion(
                    catalogo, nombre_archivo)
            case "8":
                print("Saliendo, chau!")
                break
            case _:
                print("Opción inválida, probá otra vez")


if __name__ == "__main__":
    main()
