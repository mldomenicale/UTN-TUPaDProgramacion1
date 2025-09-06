# Ejercicio 1
import random
from statistics import mode, median, mean
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto")

# Ejercicio 5
contrasena = input("Ingrese una contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Usted ha ingresado una contraseña correcta ")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("No hay sesgo")

# Ejercicio 7
frase = input("Ingrese una frase: ")
ultimo_caracter = frase[-1].lower()
if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u":
    frase += "!"
print(frase)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("Elija una opcion: ")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en MAYÚSCULA: ")
opcion = input("Ingrese 1, 2, o 3: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10
hemisferio = input("En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Ingresa el mes del año (1-12): "))
dia = int(input("Ingresa el día del mes: "))
estacion = ""
if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "invierno"
    elif hemisferio == "S":
        estacion = "verano"
elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "primavera"
    elif hemisferio == "S":
        estacion = "otoño"
elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "verano"
    elif hemisferio == "S":
        estacion = "invierno"
elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "otoño"
    elif hemisferio == "S":
        estacion = "primavera"
print(f"Usted se halla en {estacion} .")
