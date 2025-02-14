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



ciudades_norm = normalizar_datos(ciudades)
print(f"Datos sin normalizar:{ciudades}")
print(f"Datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}") 

#Usando map, con lambda:

ciudades_norm3 = list(map (lambda n: n.capitalize(),ciudades))  

print(f"Datos normalizados con map (con lambda):{ciudades_norm3}") 

    
#Ejemplo con una funcion de orden superior: map
