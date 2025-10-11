# # ejercicio 1

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# # ejercicio 2
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)

# # ejercicio 3
# frutas = list(precios_frutas.keys())
# print(frutas)

# # ejercicio 4
# contactos = {}  # creo una lista vacía
# for i in range(5):
#     nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
#     numero = input(f"Ingrese el número de {nombre}: ")
#     contactos[nombre] = numero
# # pedir nombre y mostrar asociado si es que existe.
# nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

# if nombre_buscar in contactos:
#     print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
# else:
#     print(f"No se encontró el contacto {nombre_buscar}")

# # ejercicio 5: solicita al usuario una frase e imprime:

# frase = input("Ingrese una frase: ")

# palabras = frase.split()

# palabras_unicas = set(palabras)
# print("Palabras unicas:", palabras_unicas)

# recuento = {}

# for palabra in palabras:
#     if palabra in recuento:
#         recuento[palabra] += 1
#     else:
#         recuento[palabra] = 1

# print("Recuento:", recuento)

# #ejercicio 6:
# #inicializamos un diccionario vacio.
# alumnos = {}
# for i in range(3):
#     nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

#     primera_nota = float(input(f"Ingrese la primer nota de {nombre}:"))
#     segunda_nota = float(input(f"Ingrese la segunda nota de {nombre}:"))
#     tercer_nota = float(input(f"Ingrese la tercer nota de {nombre}:"))

#     alumnos[nombre] = (primera_nota, segunda_nota, tercer_nota) #tupla

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"El promedio de {nombre} es {promedio:.2f}")

# #ejercicio 7
# parcial1 = {2, 3, 4} #uso de sets
# parcial2 = {3, 4, 5}

# ambos_parciales = parcial1 & parcial2
# print("Aprobados en ambos parciales:", ambos_parciales)

# solo_un_parcial = parcial1 ^ parcial2
# print("Aprobados solo en uno de los parciales:", solo_un_parcial)

# al_menos_un_parcial = parcial1 | parcial2
# print("Aprobados en al menos un parcial:", al_menos_un_parcial)
# # Estas operaciones de sets (intersección &, unión |, diferencia simétrica ^)
# # las vimos también en matemática (conjuntos), y yo investigué por fuera las funciones equivalentes
# # de Python para entender cómo aplicarlas en programación.

# #ejercicio 8
# productos = {}

# while True:
#     nombre = input(
#         "Ingrese el nombre del producto (o 'salir' para terminar): ")

#     if nombre.lower() == "salir":
#         break

#     if nombre in productos:
#         print(f"El stock actual de {nombre} es {productos[nombre]}")
#         agregar = int(
#             input("Ingrese cuántas unidades quiere agregar al stock: "))
#         productos[nombre] += agregar
#         print(f"Nuevo stock de {nombre}: {productos[nombre]}")
#     else:
#         stock = int(input(f"{nombre} no existe. Ingrese el stock inicial: "))
#         productos[nombre] = stock
#         print(f"{nombre} agregado con stock {stock}")

# #Ejercicio 9
# agenda = {("Lunes", "10:00"):"clase de yoga",("Miércoles", "18:00"): "Reunión escolar"}

# dia = input("Ingrese el día: ")
# hora = input("Ingrese la hora (formato HH:MM): ")

# clave = (dia, hora)

# if clave in agenda:
#     print(f"El evento programado es: {agenda[clave]}")
# else:
#     print("No hay ningún evento programado en ese horario.")

# Ejercicio 10

original = {"Francia": "París", "Italia": "Roma"}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

# las capitales son las claves. Y los países son los valores.
print("Diccionario invertido:", invertido)
