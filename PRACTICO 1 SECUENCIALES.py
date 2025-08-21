# ejercicio1
print("Hola Mundo!")

# ejercicio2
nombre = input("Ingrese su nombre: ")
saludo = (f"Hola {nombre}!")
print(saludo)

# ejercicio3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido} tengo {edad} años, y vivo en {residencia}.")

# ejercicio4
pi = 3.1416
radio = float(input("Ingrese el radio de un circulo: "))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El área del circulo es: {area}")
print(f"El perímetro del circulo es: {perimetro}")

# ejercicio 5
segundos = int(input("Ingrese un numero: "))
horas = segundos / 3600
print(f"{segundos} equivalen a {horas} horas.")

# ejercicio 6
numero = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}*{i} = {resultado}")

# ejercicio 7
num1 = int(input("Ingrese el primer numero, (que no sea 0): "))
num2 = int(input("Ingrese el segundo numero, (que no sea 0): "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es de: {suma}")
resta = num1 - num2
print(f"La resta de {num1} y {num2} es de: {resta}")
multiplicacion = num1 * num2
print(f"La multiplicacion de {num1} y {num2} es de: {multiplicacion}")
division = num1 / num2
print(f"La división de {num1} y {num2} es de: {division}")


# ejercicio 8
peso = float(input("Ingrese su peso, por favor: "))
altura = float(input("Ingrese su altura, por favor: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es, {imc}.")

# ejercicio 9
celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados farenheit es de: {fahrenheit}")

# ejercicio 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros dados, es de: {promedio}")
