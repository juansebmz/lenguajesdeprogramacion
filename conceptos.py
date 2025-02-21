import math

from functools import reduce
# #Conceptos basicos de programacion funcional
# def suma (a,b):
#     return a+b

# def resta (a,b):
#     return a-b

# def multi (a,b):
#     return a*b

# def div(a,b):
#     if b != 0:
#         return a/b
#     else:
#         print("Math Error")

# val1 = int(input("Ingrese valor 1"))
# val2 = int(input("Ingrese valor 2"))
# op = int(input("Ingrese la operación: 1. Suma 2. Resta 3. Multiplicación 4. División"))

# if op == 1:
#     operacion = suma
# elif op == 2:
#     operacion = resta
# elif op == 3:
#     operacion = multi
# elif op == 4:
#     operacion = div
# else:
#     print("Operación no válida")

# print(f"El resultado es: {operacion(val1, val2)}")


# x = suma
# y = suma

# print(x(2,5))
# print(y(6,4))

#Ejemplo: Una calculadora

#2 Funciones Puras
#3 Funciones Anonimas
# num = int(input("Ingrese un numero cualquiera: "))
# es_par = lambda x: x % 2 == 0

# print(f"{num} es par?: {es_par(num)}")






#4 Funciones de orden Superior

#4.a MAP
#Ejemplo sin map: normalizar un conjunto de datos:
ciudades = ["Cali", "medillin", "BOGOTA", "bARRANquilla"]


def normalizar_datos(lista_nombres):
    datos_norm =[]
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm


#Usando map, sin funcion lambda:

def capitalziar(palabra):
    #Retorna la palabra con la inicial en mayuscula
    return palabra.capitalize()

#map(funcion, coleccion de datos)
ciudades_norm2 = list(map(capitalziar, ciudades))



def capitalizar(palabra):
    return math.tan(palabra)

ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}") 

#Usando map, con lambda:

ciudades_norm3 = list(map (lambda n: n.capitalize(),ciudades))  

print(f"Datos normalizados con map (con lambda):{ciudades_norm3}") 

    
#Ejemplo con una funcion de orden superior: map
#Map:Aplicar una funcion a una colección de objetos



#Funcion filter aplica una funcion booleana sobre una lista de objetos, y devuelve una lista mas pequeña
edades = [12, 14, 18, 19, 24, 25, 28]

personas = [{"nombre": "Diego", "edad": "38"},
            {"nombre": "Diana", "edad": "34"},
            {"nombre": "Carolina", "edad": "36"},
            {"nombre": "Pedro", "edad": "28"}]

print(personas[0]["nombre"])

print(f"\nEdades sin filtrar: {edades}")

# La función de filtro debe ser una función booleana:
def filtrar_mayores_edad(edad):
    return edad >= 18

def filtra_personas_mayores(persona):
    return int(persona["edad"]) >= 18

mayores_edad = list(filter(filtrar_mayores_edad, edades))

# Filtrar personas mayores de edad
personas_mayores = list(filter(filtra_personas_mayores, personas))

print(f"Mayores de edad: {mayores_edad}")
print(f"Personas mayores de edad: {personas_mayores}")

numeros = list(range(1,101))

sum = 0
for i in numeros:
    sum = sum + i
    
print (sum)

suma = reduce(lambda a,b:a+b, numeros)
print(suma)


palabras = ["en","un", "lugar"]
