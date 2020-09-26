import csv
import operator

#Variables y listas a utilizar a lo largo del código

transportes =["Sea", "Air", "Rail", "Road"]
direccion =["Exports"]
direccion1 = ["Imports"]
origen =["Japan", "Germany", "China", "Italy", "USA", "Russia", "South Korea", "Netherlands", "France", "Canada", "Belgium", "Spain", "India", "United Kingdom", "Australia", "Brazil", "Switzerland", "Mexico", "Austria", "Singapore", "Vietnam", "Malaysia", "United Arab Emirates"]
ruta=[]
rutaCount=[]
rutaCount1=[]
route = []
route1 = []
frecuencia = {}
frecuencia1 = {}

contadorVia = 0
contadorDir = 0
contadorDir1 = 0
contadorPais = 0
contadorRuta = 0
x=0
z=0

totalesVia = []
totalesDir = []
totalesDir1 = []
totalesPais = []
totalesRuta = []
totalesPais1 = []
totalesPais2 = []

#Ciclo principal, donde se abre el archivo de la base de datos y se realizarán los ciclos que
#leerán y asignarán los datos a las listas

#Abrir el archivo CSV
with open ("synergy_logistics_database.csv", "r") as archivo:
    lector = csv.reader(archivo)

    #Ciclo para detectar el tipo de transporte utilizado (transporte) y el número de veces utilizado (contadorVia)
    for transporte in transportes:
        archivo.seek(0)
        for linea in lector:
            if linea[7]==transporte:
                contadorVia +=1
            
        totalesVia.append([transporte, contadorVia])
        contadorVia=0

    #Ciclos para detectar la dirección del movimiento (direction) y el número de veces realizado (contadorDir)
    #Asi mismo dentro del ciclo se almacena una tupla que contiene la ruta del movimiento (ruta) en una lista
    #(route) y cuenta el número de diferentes rutas hechas (rutaCount)
    for direction in direccion:
        archivo.seek(0)
        for linea in lector:
            if linea[1]==direction:
                contadorDir +=1
                ruta=[linea[2], linea[3]]
                route.append(tuple(ruta))                       #Se ingresa cada ruta a la lista "Route"
                if ruta not in rutaCount:                       #como tupla para luego analizar en dicc.
                    rutaCount.append(ruta)
                    
        totalesDir.append([direction, contadorDir])
        contadorDir=0

    for direction in direccion1:
        archivo.seek(0)
        for linea in lector:
            if linea[1]==direction:
                contadorDir1 +=1
                ruta=[linea[2], linea[3]]
                route1.append(tuple(ruta))                       #Se ingresa cada ruta a la lista "Route"
                if ruta not in rutaCount1:                       #como tupla para luego analizar en dicc.
                    rutaCount1.append(ruta)
                    
        totalesDir1.append([direction, contadorDir1])
        contadorDir1=0

    #Ciclo para detectar el orígen del movimiento (country), cuantos movimientos realiza (contadorPais)
    #y su aporte por movimiento (aporte)
    for country in origen:
        archivo.seek(0)
        aporte=0
        for linea in lector:
            if linea[2]==country:
                contadorPais +=1
                x=int(linea[9])                                         #Asignar el valor de cada transacción
                aporte=aporte+x                                         #para sumar el aporte de cada país

        totalesPais.append([country, contadorPais, aporte])
        contadorPais=0


#Ciclo en el cuál tomaré la información de todas las rutas y se hará un conteo de las veces que se realizaron
#despues de analizar las condiciones, se asigna cada ruta a una posición en un diccionario (frecuencia)
for n in route:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

for n in route1:
    if n in frecuencia1:
        frecuencia1[n] += 1
    else:
        frecuencia1[n] = 1



#<!-- IMPRIMIR Y ORDENAR INFORMACIÓN POR RELEVANCIA -->

#Se realizan funciones sort para mantener ordenada la información por relevancia
totalesVia= sorted(totalesVia, key=operator.itemgetter(1,0), reverse=True)

#Orden por aporte monetario
totalesPais1= sorted(totalesPais, key=operator.itemgetter(2,1,0), reverse=True)

#Orden por número de transacciones
totalesPais2= sorted(totalesPais, key=operator.itemgetter(1,2,0), reverse=True)

frecuencia= sorted(frecuencia.items(), key=lambda x: x[1], reverse = True)
frecuencia1= sorted(frecuencia1.items(), key=lambda x: x[1], reverse = True)

#La información antes recabada se prensenta en la terminal para poder ser analizada de
#forma correcta

#Vemos las diferentes rutas y la cantidad que son
#Exportación
print("Exportación : \n")
print(rutaCount, "\n")
print("Son ", len(rutaCount), " rutas \n")

#Importación
print("Importación: \n")
print(rutaCount1, "\n")
print("Son ", len(rutaCount1), " rutas \n")

#Punto 1
print("Las 10 rutas con más exportaciones son:\n")
print(frecuencia[:10], "\n")
print("Son ", len(frecuencia), "rutas \n")

print("Las 10 rutas con más importaciones son:\n")
print(frecuencia1[:10], "\n")
print("Son ", len(frecuencia1), " rutas \n")

#Punto 2
print("Las vias más utilizadas son:\n")
print(totalesVia, "\n")

print("Los movimientos totales son:\n")
print(totalesDir, totalesDir1, "\n")

#Punto 3
print("Las paises que mas aportan son:\n\nPaís | Movimientos | Aporte\n")
print(totalesPais1, "\n")
print("Las paises que mas movimientos realizan son:\n\nPaís | Movimientos | Aporte\n")
print(totalesPais2, "\n")