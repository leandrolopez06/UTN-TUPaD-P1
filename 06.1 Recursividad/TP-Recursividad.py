#Funciones Definidas
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)

def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base,exponente-1)
    
def entero_a_binario(num):
    if num == 0:
        return "0"
    elif num== 1:
        return "1"
    else:
        return entero_a_binario(num // 2) + str(num % 2)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n // 10) + n % 10

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return contar_bloques(n-1) + n 
    
def contar_digito(numero,digito):
    if numero == 0:
     return 0
    if numero % 10  == digito:
        return contar_digito(numero // 10,digito) + 1
    else:
        return contar_digito(numero // 10,digito)

#Programas Principales 

#Ejercicio 1
# num=int(input("Ingrese un numero par clcular su faactorial: "))
# print(factorial(num))

#Ejercicio 2
# num=int(input("Indique posicion de fibnacci que desea saber: "))
# print(fibonacci(num))

#Ejercicio 3
# print(potencia(10, 2))
# print(potencia(3, 4))
# print(potencia(5, 0))
# print(potencia(2, 3))

#Ejercicio 4
# num=int(input("Ingrese un numero positivo par saber su representacion en binario: "))
# print(entero_a_binario(num))

#Ejercicio 5
# palabra=input("Igrese una cadena de texto sin espacios ni tildes aa verificar si es palindromo: ")
# print(es_palindromo(palabra))

#Ejercicio 6
# num=int(input("Ingrese un numero para suar sus digitos: "))
# print(suma_digitos(num))

#Ejercicio 7
# bloques=int(input("Ingrese el numero de bloques que hay en la fila inferior: "))
# print(contar_bloques(bloques))

#Ejercicio 8
# num=int(input("Igrese un numero: "))
# digito=int(input("Igrese el digito para saber cuantas veces parece en el numero indicado"))

# print(contar_digito(num,digito))
