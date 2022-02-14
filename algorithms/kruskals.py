from collections import defaultdict

class Graph: 
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []

    def addEdge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    # uses path compression technique
    # find the root and make it the parent of i 
    # path from i to root compresses 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    # uses union by rank (rank is height)
    # attach smaller depth tree under root of deeper tree
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskals(self):
        result = [] # stores resultant MST

        i = 0 # used for sorted edges 
        e = 0 # used for result[]

        # step 1: sort edges in increasing order of weight
        # if we cant change the given graph, we can make a copy
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # create V subsets with single elements 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # number of edges to be taken is equal to V - 1
        while e < self.V - 1:
            # step 2: pick the smallest edge and increment the index for next iteration
            src, dest, weight = self.graph[i] 
            i += 1
            x = self.find(parent, src)
            y = self.find(parent, dest)

            # if including this edge does not create cycle, then include it in the resultign tree and increment index of result for next edge
            if x != y:
                e += 1
                result.append([src, dest, weight])
                self.union(parent, rank, x, y)
            # else discard the edge 
        minimumCost = 0
        print("Edges in the MST")
        for src, dest, weight in result: 
            minimumCost += weight
            print("%d -- %d == %d" % (src, dest, weight))
        print("Minimum Spanning Tree:", minimumCost)

# driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskals()




