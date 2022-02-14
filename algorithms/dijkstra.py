import sys # used to assign inf cost to all elements execpt for starting node
from heapq import heapify, heappush, heappop 

def dijkstra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
        'B':{'cost':inf,'pred':[]}, # pred = gives path from starting node (A) to that curent node
        'C':{'cost':inf,'pred':[]},
        'D':{'cost':inf,'pred':[]},
        'E':{'cost':inf,'pred':[]},
        'F':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0 
    visited = []
    current_node = src
    n = len(graph.keys()) - 1 # num times we repeat the algo for the whole graph 
    for i in range(n):
        if current_node not in visited:
            visited.append(current_node)
            min_heap = []
            for j in graph[current_node]: # determine min cost neighbor of current node 
                if j not in visited:
                    cost = node_data[current_node]['cost'] + graph[current_node][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[current_node]['pred'] + list(current_node) # using list to conc. to dict element
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        current_node = min_heap[0][1] # 0 = min element, 1 = neighbor
    
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
                    
if __name__ == "__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
    }

    source = 'A'
    destination = 'F'
    dijkstra(graph,source,destination)