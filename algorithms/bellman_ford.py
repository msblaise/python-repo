# bellman ford shortest path algorithm from src to all other vertices

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])
    
    def print_arr(self, dist):
        print("Vertex\t\tDistance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        inf = float("Inf")
        dist = [inf] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for src, dest, weight in self.graph:
                if dist[src] != inf and dist[src] + weight < dist[dest]:
                    dist[dest] = dist[src] + weight
        
        for src, dest, weight in self.graph:
            if dist[src] != inf and dist[src] + weight < dist[dest]:
                print("Graph contains negative weight cycle")
                return

        self.print_arr(dist)

g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)