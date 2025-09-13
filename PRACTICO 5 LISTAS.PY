# EJERCICIO 1
import random
notas = [6, 8, 9, 6, 4, 8, 9, 10, 7, 8]
promedio = 0
nota_max = notas[0]
nota_min = notas[0]
print(f"Notas de los estudiantes: {notas}")
for i in range(len(notas)):
    # print(notas[i])
    promedio += notas[i]
    if notas[i] < nota_min:
        nota_min = notas[i]
    if notas[i] > nota_max:
        nota_max = notas[i]


promedio /= len(notas)
print(promedio)
print(f'La nota mas alta es: {nota_max}')
print(f'La nota mas baja es: {nota_min}')

EJERCICIO 2
productos = []
for i in range(5):
    productos.append(input("Ingrese un nuevo producto: "))

lista_ordenada = sorted(productos)
print(lista_ordenada)
elemento_remove = input("Indique que producto de la lista desea eliminar: ")
if elemento_remove in lista_ordenada:
    lista_ordenada.remove(elemento_remove)
print(lista_ordenada)

EJERCICIO 3
numeros_aleatorios = [random.randint(1, 100) for i in range(15)]
pares = []
impares = []

for i in range(len(numeros_aleatorios)):
    if numeros_aleatorios[i] % 2 == 0:
        pares.append(numeros_aleatorios[i])
    else:
        impares.append(numeros_aleatorios[i])

print(f'La cantidad de numeros pares es: {len(pares)}')
print(f'La cantidad de numeros impares es: {len(impares)}')

# EJERCICIO 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetir = []
for dato in datos:
    if dato in datos_sin_repetir:
        continue
    else:
        datos_sin_repetir.append(dato)
print(datos_sin_repetir)

# EJERCICIO 5
estudiantes = ['Mateo', 'Francisco', 'Juan',
               'Juliana', 'Pedro', 'Martin', 'Laura', 'Valeria']
print(estudiantes)
opcion = input(
    'Indique el estudiante a Eliminar (si quiere agregar solo indique "+"): ')
if opcion == '+':
    estudiantes.append(input('Nombre del nuevo estudiante: '))
else:
    if opcion in estudiantes:
        estudiantes.remove(opcion)

print(estudiantes)

# EJERCICIO 6

datos = [1, 3, 5, 3, 7, 1, 9]
datos = datos[-1:] + datos[:-1]
print(datos)

# EJERCICIO 7
temperaturas_semana = [[10, 22],
                       [8, 15],
                       [13, 17],
                       [14, 19],
                       [15, 23],
                       [16, 21],
                       [17, 45]
                       ]
promedio_minima = 0
promedio_maxima = 0
max_amplitud = temperaturas_semana[0][1] - temperaturas_semana[0][0]
max_amplitud_indice = 0
# se que en la posicion 0 de cada sublista, esta la minima y en el indice 1, la maxima.

for i in range(len(temperaturas_semana)):
    print(f'Dia {i+1}: {temperaturas_semana[i]}')
    promedio_minima += temperaturas_semana[i][0]
    promedio_maxima += temperaturas_semana[i][1]
    if temperaturas_semana[i][1] - temperaturas_semana[i][0] > max_amplitud:
        max_amplitud = temperaturas_semana[i][1] - temperaturas_semana[i][0]
        max_amplitud_indice = i

promedio_maxima /= len(temperaturas_semana)
promedio_minima /= len(temperaturas_semana)

print(f'Promedio de minimas: {promedio_minima}')
print(f'Promedio de maximas: {promedio_maxima}')

print(
    f'La maxima amplitud termica se encuentra en el dia: {max_amplitud_indice + 1}')

Ejercicio 8
notas_estudiantes = [[6, 7, 10], [4, 6, 10], [5, 6, 8], [7, 8, 10], [8, 9, 10]]
promedios_estudiante = []
promedio_estudiante = 0
promedio_materia1 = 0
promedio_materia2 = 0
promedio_materia3 = 0

for i in range(len(notas_estudiantes)):
    promedio_materia1 += notas_estudiantes[i][0]
    promedio_materia2 += notas_estudiantes[i][1]
    promedio_materia3 += notas_estudiantes[i][2]
    promedio_estudiante = 0
    for j in range(len(notas_estudiantes[i])):
        promedio_estudiante += notas_estudiantes[i][j]
    promedios_estudiante.append(promedio_estudiante/len(notas_estudiantes[i]))

promedio_materia1 /= len(notas_estudiantes)
promedio_materia2 /= len(notas_estudiantes)
promedio_materia3 /= len(notas_estudiantes)
print(f"El promedio de cada estudiante es: {promedios_estudiante}")
print(f"El promedio de la materia 1 es de: {promedio_materia1}")
print(f"El promedio de la materia 2 es de: {promedio_materia2}")
print(f"El promedio de la materia 3 es de: {promedio_materia3}")

# EJERCICIO 9

tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
turno = "X"
for jugada in range(9):
    for fila_mostrar in tateti:
        # utilizo .join ya que es una forma de que el tablero quede prolijo al imprimirlo.
        print(" ".join(fila_mostrar))
    print()

    print("Turno de", turno)

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    if tateti[fila][columna] == "-":
        tateti[fila][columna] = turno
    else:
        print("La casilla ya está ocupada. Pierde su turno.")

    if turno == "X":
        turno = "O"
    else:
        turno = "X"

for fila_mostrar in tateti:
    print(" ".join(fila_mostrar))

# EJERCICIO 10
ventas = [[10, 12, 5, 8, 7, 9, 11], [5, 3, 4, 2, 6, 7, 5],
          [8, 9, 7, 10, 6, 12, 9], [6, 7, 5, 8, 7, 6, 5]]

for i in range(len(ventas)):
    print(f"Total vendido del producto {i+1}: {sum(ventas[i])}")

ventas_por_dia = []
for dia in range(7):
    total_dia = 0
    for prod in range(4):
        total_dia += ventas[prod][dia]
    ventas_por_dia.append(total_dia)

dia_max_ventas = ventas_por_dia.index(max(ventas_por_dia)) + 1
print(
    f"Día con mayores ventas totales: Día {dia_max_ventas} (Total: {max(ventas_por_dia)})")

total_por_producto = []
for i in range(4):
    total_por_producto.append(sum(ventas[i]))

producto_mas_vendido = total_por_producto.index(max(total_por_producto)) + 1
print(
    f"Producto más vendido en la semana: Producto {producto_mas_vendido} (Total: {max(total_por_producto)})")
