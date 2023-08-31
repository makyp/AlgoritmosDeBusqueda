from collections import deque

def bfs(graph, start):
    visited = set()  # conjunto para almacenar los nodos visitados
    queue = deque([start])  # cola para realizar el recorrido en amplitud
    visited.add(start)  # marcamos el nodo inicial como visitado

    while queue:
        node = queue.popleft()  # obtenemos el siguiente nodo de la cola
        print(node, end=" ")  # imprimimos el nodo actual

        # recorremos todos los vecinos del nodo actual
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # agregamos los vecinos no visitados a la cola
                visited.add(neighbor)  # marcamos los vecinos como visitados

# Ejemplo de uso, se debe modificar para atender a las solicitudes del usuario
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = input("Ingresa el vértice inicial: ")  # el usuario ingresa el vértice inicial
print("Recorrido en amplitud (BFS):")
bfs(graph, start_node)

# Imprimir el resto de los nodos en orden
for node in graph:
    if node != start_node and node not in graph[start_node]:
        print(node, end=" ")