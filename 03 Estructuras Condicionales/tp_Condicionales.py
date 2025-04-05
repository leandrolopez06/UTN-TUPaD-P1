#Ejercicio1
#edad= int(input("Ingrese su edad: " ))
#if edad >= 18:
#    print ("Es mayor de edad")

#Ejercicio2
#nota= int(input("ingrese su nota: "))
#if nota >= 6:
#    print("Aprobado")
#else:
#    print("Desaprobado")    

#Ejercicio3
# numero= int(input("Ingrese un numero: "))
# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")     

#Ejercicio4
# edad=int(input("Ingrese su edad: "))
# if edad < 12:
#     print("Niño/a")
# elif edad >=12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# elif edad >= 30:
#     print("Adulto/a")

#Ejercicio5
# contraseña=len(input("Ingrese su contraseña: "))
# if 14 >= contraseña >= 8: 
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio6
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# from statistics import mode, median, mean
# media=mean(numeros_aleatorios)
# moda=mode(numeros_aleatorios)
# mediana=median(numeros_aleatorios)
# if media > mediana and mediana > moda:
#     print("Hay sesgo positivo") 
# elif media < mediana and mediana < moda:
#     print("Hay sesgo negativo")
# elif media == mediana == moda:
#     print("No hay sesgo")

#Ejercicio7
# palabra= input("Ingrese una palabra o frase: ")
# vocales="a,e,i,o,u,A,E,I,O,U"
# esclamacion= "!"
# if palabra [-1] in vocales:
#     print(f"{palabra}{esclamacion}")
# else:
#     print(palabra)

#Ejercicio8
# nombre=input("Ingrese su nombre:")
# num=int(input("Ingrese \n 1. Si quiere su nombre en mayúsculas. \n " \
# "2. Si quiere su nombre en minúsculas. \n " \
# "3. Si quiere su nombre con la primera letra mayúscula. " ))
# if num == 1:
#     print(nombre.upper())
# elif num == 2:
#     print(nombre.lower())
# elif num == 3:
#     print(nombre.title())

#Ejercicio9
# magnitud=float(input("Ingrese la magnitud de terrremoto en escala de Richter: "))
# if magnitud < 3:
#     print("Muy leve")
# elif 3 <= magnitud < 4:
#     print("Leve")
# elif 4 <= magnitud < 5:
#     print("Moderado")
# elif 5 <= magnitud < 6:
#     print("Fuerte")
# elif 6 <= magnitud < 7:
#     print("Muy Fuerte")
# elif  magnitud >= 7:
#     print("Extremo")

#Ejercicio10
# hemisferio=input("Ingrese el hemisferio donde se encuenta N/S: ")
# mes=input("Ingrese el mes del año que es: ")
# dia=int(input("Ingrese el dia: "))
# mesInvN=("ENERO,FEBRERO")
# mesVerS=("ENERO,FEBRERO")
# mesInvS=("JULIO,AGOSTO")
# mesVerN=("JULIO,AGOSTO")
# mesPriN=("ABRIL,MAYO")
# mesOtoS=("ABRIL,MAYO")
# mesPriS=("OCTUBRE,NOVIEMBRE")
# mesOtoN=("OCTUBRE,NOVIEMBRE")
 
# if hemisferio.upper() == "N" and  ((mes.upper() == "DICIEMBRE" and 21 < dia <= 31) or (mes.upper() in mesInvN) or (mes.upper()== "MARZO" and 1 < dia <= 20)):
#     print("Invierno")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "DICIEMBRE" and 21 < dia <= 31) or (mes.upper() in mesVerS) or (mes.upper()== "MARZO" and 1 < dia <= 20)):  
#     print("Verano")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "JUNIO" and 21 < dia <= 30) or (mes.upper() in mesInvS) or (mes.upper()== "SEPTIEMBRE" and 1 < dia <= 20)):
#     print("Invierno")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "JUNIO" and 21 < dia <= 30) or (mes.upper() in mesVerN) or (mes.upper()== "SEPTIEMBRE" and 1 < dia <= 20)):
#     print("Verano")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "MARZO" and 21 < dia <= 31) or (mes.upper() in mesPriN) or (mes.upper()== "JUNIO" and 1 < dia <= 20)):
#     print("Primavera")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "MARZO" and 21 < dia <= 31) or (mes.upper() in mesOtoS) or (mes.upper()== "JUNIO" and 1 < dia <= 20)):
#     print("Otoño")
# elif  hemisferio.upper() == "S" and  ((mes.upper() == "SEPTIEMBRE" and 21 < dia <= 30) or (mes.upper() in mesPriS) or (mes.upper()== "DICIEMBRE" and 1 < dia <= 20)):
#     print("Primavera")
# elif  hemisferio.upper() == "N" and  ((mes.upper() == "SEPTIEMBRE" and 21 < dia <= 30) or (mes.upper() in mesOtoN) or (mes.upper()== "DICIEMBRE" and 1 < dia <= 20)):
#     print("Otoño")