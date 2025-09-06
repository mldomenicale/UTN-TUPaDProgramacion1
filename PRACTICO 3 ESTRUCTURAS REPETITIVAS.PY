# EJERCICIO 1
import random
for i in range(101):
    print(i)

# EJERCICIO 2

numero = int(input("Ingrese un numero entero: "))
digitos = 1
while numero > 10:
    numero = numero // 10
    digitos += 1
print(digitos)

# EJERCICIO 3

valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(valor_1 + 1, valor_2):
    suma += i
print(suma)

# EJERCICIO 4

num = int(input("Ingrese un numero entero para sumar: (0 para terminar)"))
suma = num
while num != 0:
    num = int(input("Ingrese un numero entero para sumar: (0 para terminar)"))
    suma += num
print(suma)

# Ejercicio 5

num_ale = random.randint(0, 9)
num = int(input("Intente adivinar el número (0 a 9): "))
intento = 1
while num != num_ale:
    num = int(input("Intente adivinar el número (0 a 9): "))
    intento += 1
print(f"Usted logro adivinar el numero {num_ale} en {intento} intentos")

# Ejercicio 6

for i in range(100, 0, -2):
    print(i)

# Ejercicio 7

valor1 = 0
valor2 = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(valor1, valor2 + 1):
    suma = suma + i
print(suma)

# EJERCICIO 8
positivo = 0
negativo = 0
par = 0
impar = 0
rango = 100
for i in range(rango):
    num = int(input("Ingrese un número: "))
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    num = abs(num)
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Usted ha ingresado: {positivo} numeros positivos.")
print(f"Usted ha ingresado: {negativo} numeros negativos.")
print(f"Usted ha ingresado: {par} numeros pares.")
print(f"Usted ha ingresado: {impar} numeros impares.")

# EJERCICIO 9
rango = 100
media = 0
for i in range(rango):
    num = int(input("Ingrese un número: "))
    media += num

media /= rango
print(f"La media es de : {media}")

# EJERCICIO 10

numero = int(input("Ingresa un número: "))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print("Número invertido:", invertido)
