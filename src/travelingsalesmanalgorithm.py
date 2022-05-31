import matplotlib.pyplot as plt
import math
import copy
import random
import numpy as np
import time
from numba import njit,jit

def read_data_from_file(name):
    lista=[]
    with open (name) as pl :
        for line in pl :
            lista.append( (int(line.split(" ")[0]),int(line.split(" ")[1])) )
    return np.array(lista)

@njit
def distance(lista):
    distance = 0
    for i in range(lista.shape[0]-1):
        distance += math.sqrt(  (lista[i][0] - lista[i+1][0])**2 + (lista[i][1] - lista[i+1][1])**2  )
    distance += math.sqrt(  (lista[lista.shape[0]-1][0] - lista[0][0])**2 + (lista[lista.shape[0]-1][1] - lista[0][1])**2  )
    return distance

@njit
def algorith(lista, MAX_IT):
    for i in range(100, 0, -1):
        T = 0.001*i**2
        for it in range(0, MAX_IT+1):
            newLista = np.copy(lista)
            a = c = random.randint(0, lista.shape[0]-2)
            while c == a or c == a+1 or c == a-1:
                c = random.randint(0, lista.shape[0]-2)
            newLista[a+1],newLista[c] = newLista[c].copy(),newLista[a+1].copy()
            if distance(newLista) < distance(lista):
                lista = np.copy(newLista)
            else:
                r = random.random()
                if r < math.exp(-1.0 * (distance(newLista) - distance(lista))/T):
                    lista = np.copy(newLista)
    return lista

# lista=read_data_from_file('src/data.dat')
# plt.plot([i[0] for i in lista],[i[1] for i in lista], linestyle='-', marker='o', color='red')
# plt.savefig('src/__imgcache__/traveling_1.png')
# plt.close()
# start_cycle_length=distance(lista)
# start = time.time()
# lista=algorith(lista, 10000) 
# # MAX_IT: 500 000, TIME: 66s DISTANCE: 2072
# # MAX_IT: 1 000 000, TIME: 134s DISTANCE: 2006
# end = time.time()
# print(end - start)
# end_cycle_length=distance(lista)
# plt.plot([i[0] for i in lista],[i[1] for i in lista], linestyle='-', marker='o', color='red')
# plt.savefig('src/__imgcache__/traveling_2.png')
# plt.close()