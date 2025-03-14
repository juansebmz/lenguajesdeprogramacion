from functools import reduce

def loadData(filePath):
    with open (filePath, mode="r", encoding="utf-8")as file:
        headers = file.readline().strip().split(",")
        for line in file:
            values = line.strip().split(",")
            record= dict(zip(headers,values))
            yield record

def nivel(n):
    n["nivel"] = int(n["nivel"])
    return n
            

def filter10N(x):
    return x["nivel"] > 10


dataStream = loadData("dataset.csv")

dataLocal = []

try:
    for __ in range (1000):
        dataLocal.append(next(dataStream))
except:
    print("No hay más datos")
    
#print(dataLocal)

#filtrar personajes con nivel > 10 usando una función lambda

listarNivel = list(map(nivel,dataLocal))

listaMayores = list(filter(filter10N,listarNivel))

#print(listaMayores)

#sumar el ataque y la defensa en una funcion lambda en "totalPower"

totalPower = list(map(lambda x: {**x, "totalPower": int(x["ataque"]) + int(x["defensa"])}, listaMayores))

#print(totalPower)

# obtener el personaje con mayor poder total de todo el dataset usando reduce
mayorPoder = reduce(lambda x,y: x if int(x["totalPower"]) > int(y["totalPower"]) else y, totalPower)

#print(mayorPoder)