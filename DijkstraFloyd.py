# Óscar Javier Villeda Arteaga  -  A01277297
# Ximena Cantera Reséndiz       -  A01277310

import sys

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0
    
    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i
        visited[min_index] = True
        for j in range(n):
            if graph[min_index][j] != -1 and distance[j] > distance[min_index] + graph[min_index][j]:
                distance[j] = distance[min_index] + graph[min_index][j]
    
    return distance


def floyd_warshall(graph):
    n = len(graph)
    dist = [[0] * n for _ in range(n)]
    
    # Inicializar la matriz de distancias con los valores del grafo
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                dist[i][j] = sys.maxsize
            else:
                dist[i][j] = graph[i][j]
    
    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


def main():
    n = int(input("Ingrese el número de nodos: "))
    print("Ingrese la matriz de adyacencia:")
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    print("\nDistancias mínimas usando Dijkstra:")
    for i in range(n):
        distances = dijkstra(graph, i)
        print(f"Desde el nodo {i}: {distances}")
    
    print("\nDistancias mínimas usando Floyd-Warshall:")
    distancias_floyd = floyd_warshall(graph)
    for fila in distancias_floyd:
        print(" ".join(map(str, fila)))


if __name__ == "__main__":
    main()