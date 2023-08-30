import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def create_graph():
    graph = {}
    num_edges = int(input("Ingrese el número de conexiones: "))
    
    for _ in range(num_edges):
        source, target = input("Ingrese una conexión (nodo fuente nodo destino): ").split()
        if source not in graph:
            graph[source] = []
        if target not in graph:
            graph[target] = []
        graph[source].append(target)
    
    return graph

def visualize_graph(graph):
    G = nx.DiGraph(graph)
    nx.draw(G, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_color="black")
    plt.show()

def main():
    graph = create_graph()
    start_node = input("Ingrese el nodo de inicio para DFS: ")
    visited = set()
    print("Recorrido DFS:")
    dfs(graph, start_node, visited)
    
    visualize_graph(graph)

if __name__ == "__main__":
    main()
