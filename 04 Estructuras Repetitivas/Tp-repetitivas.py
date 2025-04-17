#Ejercicio 1
for x in range (0,101):
     print(x)

#Ejercicio 2 
num= int(input("Ingrese un numero entero: "))
if num >= 0:
     cantiDig= len(str(num))
     print(f"la cantida de digitos que contiene es {cantiDig}")
else:
     cantiDig = len(str(num))- 1
     print(f"la cantida de digitos que contiene es {cantiDig}")


#Ejercicio 3
num1=int(input("Ingrese el primer valor: "))
num2=int(input("ingrese el segundo valor: "))
sumatoria=0
for x in range (num1+1,num2):
     sumatoria += x
print(sumatoria)

#Ejecicio 4
suma=0
num=int(input("Ingrese un numero: "))
while num != 0:
     suma += num
     num=int(input("Ingrese otro numero: "))
     if num== 0:
           print(f"El total acumulado es {suma}") 

#Ejercicio 5
import random
numeros_alea = [random.randint(0,9) for i in range(1)]
print(numeros_alea)
intentos=1
num=int(input("Ingrese un numero: ")) 
while num not in numeros_alea:
     intentos +=1
     num=int(input("Usted no acertó,ingrese otro numero: "))
if num in numeros_alea:
     print(f"Usted acertó el numero correcto es {numeros_alea} y lo hizo en {intentos} intentos")

#Ejercicio 6
for x in range (100,-1,-2):
     print(x)

#Ejercicio 7
num=int(input("ingrese un numero: "))
sumatoria=0
for x in range (0,num+1):
     sumatoria += x
print(f"La suma de los numero comprendidos ente el 0 y {num} es {sumatoria}")

#Ejercicio 8
numPar=0
numImp=0
numPos=0
numNeg=0
for x in range (0,100):
     num=int(input("Ingrese un numero entero: "))
     if num > 0:
         numPos += 1 
     if num < 0:
         numNeg += 1
     if num % 2 == 0:
         numPar += 1
     if num % 2 != 0:
         numImp += 1   
print (f"Numeros pares ingresados = {numPar} \n"
        f"Numeros Impares ingresados = {numImp} \n" 
        f"Numeros negativos ingresados = {numNeg} \n" 
        f"Numeros positivos ingresados = {numPos}")

#Ejercicio 9
suma=0
for x in range (1,101):
     num=int(input("ingrese un numero entero: "))
     suma += num 
media=suma/x
print(media)
    
#Ejercicio 10
numero= int(input("ingrse numero entero: "))
numInv= 0
while numero > 0:
     numInv = numInv * 10 + numero % 10
     numero //= 10
print (numInv)