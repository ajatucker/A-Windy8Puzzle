#Ryan Schanerberger & Alexis Tucker
#CIS 479
#Windy 8-Puzzle
from array import*
from heapq import*
import itertools
import queue

#pq = array('i', []);

class pq:
   def __init__(self):
         self.minHeap = []
   #return top priority item
   def peek(self):
      return self.minHeap[0]
   #insert an item into the heap
   def insert(self, item):
      heappush(self.minHeap, item)
   #pops the top item of the heap 
   def remove(self):
      heappop(self.minHeap)
      heapify(self.minHeap)
   #prints if queue is empty
   def isEmpty(self):
      return len(self.minHeap) == True
   #need to full print heap
   def printHeap(self):
      for i in self.minHeap:
            print(i, end = ' ')
            print()
         

heapObj = pq()
heapObj.insert(3)
heapObj.insert(2)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45)
heapObj.remove()
   
#print(heapObj.peek())

#heapObj.printHeap()

#print(heapObj.isEmpty())

#heapObj.remove()
#heapObj.remove()

#heapObj.printHeap()

class aGraph:
   def __init__(self, edges, n):
      self.adj = [[] for _ in range(n)]
      
      for(s, d) in edges:
         self.adj[s].append(d)
#Add vertex to adjacency list
   def addVertex(self, v):
      if v not in self.adj:
         self.adj[v] = []
#Add an edge
   def addEdge(self, edge):
      edge = set(edge)
      (v1, v2) = tuple(edge)
      if v1 in self.gDict:
         self.gDict[v1].append(v2)
      else:
         self.gDict[v1] = [v2]
   def swapVertex(self, v1, v2):
      swapped = False
      if self.adj[v1] != 0 and self.adj[v2] != 0:
         x = self.adj[v1]
         y = self.adj[v2]
         self.adj[v2] = x
         self.adj[v1] = y
         #self.adj[v1][x] = [v2]
         swapped = True
      return swapped
            
#List the edges of graph
   def findEdges(self):
      edgename = []
      for vx in self.gDict:
         for nxtvx in self.gDict[vx]:
            if {nxtvx, vx} not in edgename:
               edgename.append({vx, nxtvx})
      return edgename
#print the adjacency matrix
   def printGraph(self):
    for src in range(len(self.adj)):
        for dest in self.adj[src]:
            if dest == 0 or src == 0:
               print(f'( - —> {dest}) ', end='')
            else:
               print(f'({src} —> {dest}) ', end='')
        print()

#initial state
initArr = [[2, 8, 3], [6, 7, 4], [1, 5, 0]]
#2, 8, 3
#6, 7, 4
#1, 5, 0
#goal state
goalArr = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#1, 2, 3
#8, 0, 4
#7, 6, 5

# Create the dictionary with graph elements
initialSt = [(2, 8), (2, 6), (8, 2), (8, 3),(8,7), (3,8), (3,4), (7, 6), (7,8), (7, 4), (7,5), (4, 7), (4, 3), (4, 0),
 (1, 6), (1,5), (5, 1), (5, 7), (5,0), (0,5), (0,4)]

numOfVertices = 9

g = aGraph(initialSt, numOfVertices)
#print(g.getVertices())
#print(g.getEdges())

#g.printGraph()

print(g.swapVertex(1, 2))

g.printGraph()


