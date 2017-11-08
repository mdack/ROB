#! usr/bin/python

from Grafo import *

grafo = Grafo();

agregar(grafo, "Oradea")
agregar(grafo, "Zerind")
agregar(grafo, "Arad")
agregar(grafo, "Timisoara");
agregar(grafo, "Lugoj");
agregar(grafo, "Mehadia");
agregar(grafo, "Dobreta");
agregar(grafo, "Sibiu");
agregar(grafo, "Fagaras");
agregar(grafo, "Rimnicu Vilcea");
agregar(grafo, "Pitesti");
agregar(grafo, "Craiova");
agregar(grafo, "Bucharest");
agregar(grafo, "Giurgiu");
agregar(grafo, "Urziceni");
agregar(grafo, "Vasiul");
agregar(grafo, "Iasi");
agregar(grafo, "Neamt");
agregar(grafo, "Hirsova");
agregar(grafo, "Eforle");

relacionar(grafo, "Oradea", "Zerind", 71);
relacionar(grafo, "Oradea", "Sibiu", 151);
relacionar(grafo, "Zerind", "Arad", 75);
relacionar(grafo, "Arad", "Timisoara", 118);
relacionar(grafo, "Timisoara", "Lugoj", 111);
relacionar(grafo, "Lugoj", "Mehadia", 70);
relacionar(grafo, "Mehadia", "Dobreta", 75);
relacionar(grafo, "Dobreta", "Craiova", 120);
relacionar(grafo, "Craiova", "Rimnicu Vilcea", 146);
relacionar(grafo, "Craiova", "Pitesti", 138);
relacionar(grafo, "Sibiu", "Rimnicu Vilcea", 80);
relacionar(grafo, "Sibiu", "Fagaras", 99);
relacionar(grafo, "Rimnicu Vilcea", "Pitesti", 97);
relacionar(grafo, "Pitesti", "Bucharest", 101);
relacionar(grafo, "Fagaras", "Bucharest", 211);
relacionar(grafo, "Bucharest", "Urziceni", 85);
relacionar(grafo, "Urziceni", "Hirsova", 98);
relacionar(grafo, "Hirsova", "Eforle", 86);
relacionar(grafo, "Urziceni", "Vasiul", 142);
relacionar(grafo, "Vasiul", "Iasi", 92);
relacionar(grafo, "Iasi", "Neamt", 87);

cadena = input("Introduce nodo destino: ")

dijkstra(grafo, "Bucharest", cadena)




