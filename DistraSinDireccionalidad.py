import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, value):
        self.nodes.append(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.nodes[from_node].append((to_node, weight))
        self.nodes[to_node].append((from_node, weight))  # If the graph is undirected


    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]
        previous_nodes = {node: None for node in self.nodes}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous_nodes

    def shortest_path(self, start, end, previous_nodes):
        path = []
        while end:
            path.append(end)
            end = previous_nodes[end]
        return path[::-1]

def main():
    while True:
        graph = Graph()

        num_nodes = int(input("Ingrese el número de nodos: "))
        for i in range(num_nodes):
            node_value = input(f"Ingrese el valor para el nodo {i}: ")
            graph.add_node(node_value)

        num_edges = int(input("Ingrese el número de aristas: "))
        for _ in range(num_edges):
            from_node = input("Ingrese el nodo de inicio de la arista: ")
            to_node = input("Ingrese el nodo de destino de la arista: ")
            weight = float(input("Ingrese el peso de la arista: "))
            graph.add_edge(from_node, to_node, weight)

        G = nx.DiGraph()
        for node in graph.nodes:
            G.add_node(node)
        for from_node, edges in graph.edges.items():
            for to_node, weight in edges:
                G.add_edge(from_node, to_node, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, node_color='lightblue')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        start_node = input("Ingrese el nodo de inicio para el algoritmo de Dijkstra: ")
        end_node = input("Ingrese el nodo de destino: ")
        distances, previous_nodes = graph.dijkstra(start_node)
        shortest_path = graph.shortest_path(start_node, end_node, previous_nodes)

        print(f"Distancia más corta desde {start_node} hasta {end_node}: {distances[end_node]}")
        print(f"Camino más corto: {' -> '.join(shortest_path)}")

        plt.show()

        another_route = input("¿Desea conocer otra ruta? (Sí/No): ")
        if another_route.lower() != "si" and another_route.lower() != "sí":
            break

if __name__ == "__main__":
    main()
