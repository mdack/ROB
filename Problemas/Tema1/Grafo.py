#! usr/bin/python

class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)

class Arista(object):
    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso        
    def __str__(self):
        return str(self.elemento) + str(self.peso)

 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2, peso = 1):
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)
    
def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append(Arista(destino, peso)) 

costeMejor = 99999
sol = []

def dijkstra(grafo, origen, destino):
    pesos = []
    coste = 0

    for i in grafo.relaciones:
        if i == origen:
            sol.append(origen)
            pesos.append(origen)
            dijkstraAux(grafo, grafo.relaciones[i], destino, pesos, coste)
            sol.append(destino)
            print(sol)
            print("Coste total: ", costeMejor)
            return
            

def dijkstraAux(grafo,elem, destino,lista, coste):
    global costeMejor
    global sol

    for j in elem:
        if j.elemento not in lista:
            if j.elemento == destino:
               if coste < costeMejor:
                   costeMejor = coste
                   sol = lista[:]
            else:
               coste = coste + j.peso
               lista.append(j.elemento)
               aux = buscaNodo(grafo, j.elemento)
               dijkstraAux(grafo, aux, destino, lista, coste)
               coste = coste - j.peso
               lista.remove(j.elemento)



def buscaNodo(grafo, nodo):

    for k in grafo.relaciones:
        if k == nodo:
            return grafo.relaciones[k]
