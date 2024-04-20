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