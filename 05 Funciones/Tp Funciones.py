#Funciones Definidas
def imprimir_hola_mundo():
    return print("Hola Mundo!")
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")
def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
def calcular_area_circulo(radio):
    import math 
    area=math.pi*(radio**2)
    return area
def calcular_perimetro_circulo(radio):
    import math
    perimetro=2*math.pi*radio
    return perimetro
def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas
def tabla_de_multiplicar(multiplicador):
    for i in range(1,11):
        producto=i*multiplicador
        tabla=print(f"{i}x{multiplicador}={producto}")
    return tabla
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    resultado=(f"suma={suma}",f"resta={resta}",f"multiplicaion={multiplicacion}",f"division={division}")
    return resultado
def calcular_imc(peso,altura):
    imc=peso/(altura**2)
    return imc
def celsius_a_fahrenheit(celcius):
    fahrenheit=celcius*9/5+32
    return fahrenheit
def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio



#Pograma Pricipal

#Ejercicio 1
imprimir_hola_mundo()

#Ejercicio 2 
saludar_usuario("Leandro")

#Ejercicio 3
a=input("ingrese su nombre: ")
b=input("ingrese su apellido: ")
c=input("ingrese su edad: ")
d=input("ingrese su lugar de residencia: ")

informacion_personal(a,b,c,d)

#Ejercicio 4
radio=int(input("Ingrese el radio de su circulo: "))

area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)

print(f"El Area del circulo es: {area} y el perimetro es: {perimetro}")

#Ejercicio 5
segundos=int(input("Ingrese la cantidad de segundos: "))

horas=segundos_a_horas(segundos)
print(f"{segundos} segundos equivale a {horas} horas")

#Ejercicio 6
multiplicador=int(input("ingrese un numero: "))

tabla_de_multiplicar(multiplicador)

#Ejercicio 7
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

operaciones_basicas(a,b)

#Ejercicio 8
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en mts: "))

resultado=calcular_imc(peso,altura)
print(f"Su indice de masa corporal(IMC) es {resultado:.2f}")

#Ejercicio 9
celcius=float(input("Ingrese los grados celcius: "))

fahrenheit=celsius_a_fahrenheit(celcius)
print(f"{celcius} grados Celcius equivalen a {fahrenheit} grados fahrenheit")

#Ejercicio 10
a=float(input("Ingrese la primera nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrese la tercera nota: "))

promedio=calcular_promedio(a,b,c)
print(f"el prmedio de las notas ingresadas es: {promedio}")