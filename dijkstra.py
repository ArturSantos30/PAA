import sys
 
class Graph():
 
   def __init__(self, vertices):
       self.V = vertices
       self.graph = [[0 for column in range(vertices)]
                   for row in range(vertices)]
 
   def printSolution(self, dist):
       print ("Vertice \tDistancia da origem")
       for node in range(self.V):
           print (node, "\t", dist[node])
 
   def minDistance(self, dist, visited):
       min = sys.maxsize
       for v in range(self.V):
           if dist[v] < min and visited[v] == False:
               min = dist[v]
               min_index = v
       return min_index
 
   def dijkstra(self, src):
       dist = [sys.maxsize] * self.V
       dist[src] = 0
       visited = [False] * self.V
 
       for _ in range(self.V):
           u = self.minDistance(dist, visited)
 
           visited[u] = True
 
           for v in range(self.V):
               if self.graph[u][v] > 0 and visited[v] == False and \
               dist[v] > dist[u] + self.graph[u][v]:
                       dist[v] = dist[u] + self.graph[u][v]
 
       self.printSolution(dist)
 
grafo = Graph(6)
grafo.graph = [[0, 4, 2, 0, 0, 0],
       [4, 0, 1, 5, 0, 0],
       [2, 1, 0, 8, 10, 0],
       [0, 5, 8, 0, 2, 6],
       [0, 0, 10, 2, 0, 2],
       [0, 0, 0, 6, 2, 0]];
 
grafo.dijkstra(0);