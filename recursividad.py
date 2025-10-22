# EJERCICIO 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingrese un número entero positivo: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# EJERCICIO 2


def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)


n = int(input("Ingrese la posición máxima de la serie de Fibonacci: "))
print("Serie de Fibonacci: ")
for i in range(n + 1):
    print(fibonacci(i), end=" ")

# EJERCICIO 3


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")

# EJERCICIO 4


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Ingrese un numero entero positivo: "))
if num == 0:
    binario = "0"
else:
    binario = decimal_a_binario(num)

print(f"El número {num} en binario es: {binario}")

# EJERCICIO 5


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False

    return es_palindromo(palabra[1:-1])


print(es_palindromo("oso"))
print(es_palindromo("cuaderno"))
print(es_palindromo("tiza"))
print(es_palindromo("neuquen"))

# EJERCICIO 6


def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(304))

# EJERCICIO 7


def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))
print(contar_bloques(5))

# EJERCICIO 8


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))

# fin
