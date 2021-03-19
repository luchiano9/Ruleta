import random
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt


#Parametros
cantTiradas = 10

#Variables (no tocar)
probabilidadIndiv = 1/38 
promedioTiradas =   666/38
resultados = []
frecRelativas = []
numero = 0 
tiradas = 0
suma = 0

def ValidInput(txt,min,max):
    value = int(input(txt))
    while value < min or value > max:
        value = int(input(txt))

    return value

def Comienzo(resultados,numero,frecRelativas,tiradas,suma):
    cantTiradas = ValidInput("Ingrese cantidad de tiradas: ", 0, 10)
    numElegido = ValidInput("Ingrese numero a estudiar (0-36): ", 0, 36)

    frecAbs = 0

    while  (tiradas < cantTiradas):
        numActual = random.randint(0,37)
        resultados.append(numActual)

        suma += numActual
        tiradas += 1

        if numActual == numElegido:
            frecAbs += 1

        frecRelativas.append(frecAbs/tiradas)

    Resultados(resultados,numero,frecRelativas) 

def Resultados(resultados,numero,frecRelativas):
    for frecRelativa in frecRelativas:
        print (frecRelativa)

    promedio = np.mean(resultados)
    print ("El valor promedio es ",promedio)
    desviacion = np.std(resultados)
    print ("La desviacion tipica es ",desviacion)
    plt.plot(resultados, label = "Resultados")
    plt.title("Ruleta")
    plt.xlabel("Tiradas")
    plt.ylabel("Valores")
    
    plt.ioff()
    plt.plot(frecRelativas, label= "Frecuencias relativas")
    plt.legend(loc="upper left")
    plt.show()
    plt.ion()
    plt.plot(frecRelativas)
    

Comienzo(resultados,numero,frecRelativas,tiradas,suma)
