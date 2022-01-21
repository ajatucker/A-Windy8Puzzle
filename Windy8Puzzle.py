#Ryan Schanerberger & Alexis Tucker
#CIS 479
#Windy 8-Puzzle
from array import*
from heapq import*
import itertools
import queue

#pq = array('i', []);

class pq:
   def __init__(self, minHeap = None):
       if minHeap is None:
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
   #need to full print heap


heapObj = pq()
heapObj.insert(2)
heapObj.insert(3)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45) 
   
print(heapObj.peek())

class aGraph:
   def __init__(self,gDict=None):
      if gDict is None:
         gDict = {}
      self.gDict = gDict
   def getVertices(self):
      return list(self.gDict.keys())
   def getEdges(self):
      return self.findEdges()
#Add vertex
   def addVertex(self, v):
      if v not in self.gDict:
         self.gDict[v] = []
#Add an edge
   def addEdge(self, edge):
      edge = set(edge)
      (v1, v2) = tuple(edge)
      if v1 in self.gDict:
         self.gDict[v1].append(v2)
      else:
         self.gDict[v1] = [v2]
#List the edges of graph
   def findEdges(self):
      edgename = []
      for vx in self.gDict:
         for nxtvx in self.gDict[vx]:
            if {nxtvx, vx} not in edgename:
               edgename.append({vx, nxtvx})
      return edgename

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
initialSt = { 
   "2" : ["8","6"],
   "8" : ["2", "3", "7"],
   "3" : ["8", "4"],
   "6" : ["7", "1"],
   "7" : ["6", "8", "4", "5"],
   "4" : ["7", "3", "0"] ,
   "1" : ["6", "5"],
   "5" : ["1", "7", "0"],
   "0" : ["5", "4"]
}

g = aGraph(initialSt)
#print(g.getVertices())
#print(g.getEdges())

#print(goalArr)


