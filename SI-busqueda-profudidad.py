class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for edge in edges:
            self.adjList[edge.src].append(edge.dest)
            self.adjList[edge.dest].append(edge.src)

def DFS(graph, v, discovered):
    discovered[v] = True
    print(v, end=" ")  # Imprime el nodo actual
    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

# Ejemplo de uso
if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 3), Edge(1, 4)]
    n = 5  # Número total de nodos
    graph = Graph(edges, n)
    discovered = [False] * n  # Lista para rastrear los nodos descubiertos
    start_node = 0  # Nodo inicial
    DFS(graph, start_node, discovered)