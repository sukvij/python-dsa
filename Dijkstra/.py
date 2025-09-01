# minHeap is used here bro.....
import heapq
class Edge:
    def __init__(self, u, v, weight):
        self.From = u
        self.To = v
        self.Weight = weight

class Graph:
    def __init__(self, ver):
        self.Vertices = ver
        self.Edges = [[] for _ in range (0, ver)]

    def add_edge(self, u, v, weight):
        self.Edges[u].append(Edge(u, v, weight))
        self.Edges[v].append(Edge(v, u, weight))
    
    def DijkstraAlgorithm(self, src):
        visited = [False for _ in range (self.Vertices)]
        distance = [float(10000000) for _ in range (self.Vertices)]
        # print(visited, distance)
        distance[src] = 0
        heap = []
        heapq.heappush(heap, (-100000, src))

        while heap:
            weight, u = heapq.heappop(heap)
            if visited[u]:
                continue

            visited[u] = True
            for child in self.Edges[u]:
                distance[child.To] = min(distance[child.To], distance[child.From] + child.Weight)
                if visited[child.To] == False:
                    heapq.heappush(heap, (child.Weight, child.To))
            print(distance)
        

g = Graph(7)

# The user's provided graph edges
g.add_edge(3, 0, 4) 
g.add_edge(3, 4, 2)
g.add_edge(0, 2, 3)
g.add_edge(0, 4, 4)
g.add_edge(4, 2, 4)
g.add_edge(4, 6, 5)
g.add_edge(2, 5, 5)
g.add_edge(2, 1, 2)
g.add_edge(1, 5, 2)
g.add_edge(6, 5, 5)
g.DijkstraAlgorithm(0)